try:
    from Crypto.Hash import keccak

    def sha3_256(x): return keccak.new(digest_bits=256, data=x).digest()
except ImportError:
    import sha3 as _sha3

    def sha3_256(x): return _sha3.keccak_256(x).digest()


from functools import wraps
import hashlib
from hashlib import sha256
import re

import six

if six.PY3:
    long = int


def ensure_bytes(data):
    if not isinstance(data, six.binary_type):
        return data.encode('utf-8')
    return data


def ensure_str(data):
    if isinstance(data, six.binary_type):
        return data.decode('utf-8')
    elif not isinstance(data, six.string_types):
        raise ValueError("Invalid value for string")
    return data


def chr_py2(num):
    """Ensures that python3's chr behavior matches python2."""
    if six.PY3:
        return bytes([num])
    return chr(num)


def hash160(data):
    """Return ripemd160(sha256(data))"""
    rh = hashlib.new('ripemd160', sha256(data).digest())
    return rh.digest()


def is_hex_string(string):
    """Check if the string is only composed of hex characters."""
    pattern = re.compile(r'[A-Fa-f0-9]+')
    if isinstance(string, six.binary_type):
        string = str(string)
    return pattern.match(string) is not None


def long_to_hex(l, size):
    """Encode a long value as a hex string, 0-padding to size.

    Note that size is the size of the resulting hex string. So, for a 32Byte
    long size should be 64 (two hex characters per byte"."""
    f_str = "{0:0%sx}" % size
    return ensure_bytes(f_str.format(l).lower())


def long_or_int(val, *args):
    return long(val, *args)


def memoize(f):
    """Memoization decorator for a function taking one or more arguments."""
    def _c(*args, **kwargs):
        if not hasattr(f, 'cache'):
            f.cache = dict()
        key = (args, tuple(kwargs))
        if key not in f.cache:
            f.cache[key] = f(*args, **kwargs)
        return f.cache[key]
    return wraps(f)(_c)



def to_string(value):
    if isinstance(value, bytes):
        return value
    if isinstance(value, str):
        return bytes(value, 'utf-8')
    if isinstance(value, int):
        return bytes(str(value), 'utf-8')
        

def sha3(seed):
    return sha3_256(to_string(seed))



def big_endian_to_int(value: bytes) -> int:
    return int.from_bytes(value, "big")




def checksum_encode(addr): # Takes a 20-byte binary address as input
    o = ''
    v = big_endian_to_int(sha3(addr.hex()))
    for i, c in enumerate(addr.hex()):
        if c in '0123456789':
            o += c
        else:
            o += c.upper() if (v & (2**(255 - 4*i))) else c.lower()
    return '0x'+o



def checksummed(addrstr):
    return checksum_encode(bytes.fromhex(addrstr[2:]))


# def test(addrstr):
#     assert(addrstr == checksum_encode(bytes.fromhex(addrstr[2:])))
