import random
from .py2specials import *
from .py3specials import *
from bisect import bisect_left

wordlist_english=list(open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'english.txt'),'r'))

def eint_to_bytes(entint,entbits):
    a=hex(entint)[2:].rstrip('L').zfill(32)
    print(a)
    return binascii.unhexlify(a)

def mnemonic_int_to_words(mint,mint_num_words,wordlist=wordlist_english):
    backwords=[wordlist[(mint >> (11*x)) & 0x7FF].strip() for x in range(mint_num_words)]
    return backwords[::-1]

def entropy_cs(entbytes):
    entropy_size=8*len(entbytes)
    checksum_size=entropy_size//32
    hd=hashlib.sha256(entbytes).hexdigest()
    csint=int(hd,16) >> (256-checksum_size)
    return csint,checksum_size

def entropy_to_words(entbytes,wordlist=wordlist_english):
    if(len(entbytes) < 4 or len(entbytes) % 4 != 0):
        raise ValueError("The size of the entropy must be a multiple of 4 bytes (multiple of 32 bits)")
    entropy_size=8*len(entbytes)
    csint,checksum_size = entropy_cs(entbytes)
    entint=int(binascii.hexlify(entbytes),16)
    mint=(entint << checksum_size) | csint
    mint_num_words=(entropy_size+checksum_size)//11

    words = mnemonic_int_to_words(mint,mint_num_words,wordlist)
    return ' '.join(words)

def words_bisect(word,wordlist=wordlist_english):
    lo=bisect_left(wordlist,word)
    hi=len(wordlist)-bisect_left(wordlist[:lo:-1],word)

    return lo,hi

def words_split(wordstr,wordlist=wordlist_english):
    def popword(wordstr,wordlist):
        for fwl in range(1,9):
            w=wordstr[:fwl].strip()
            lo,hi=words_bisect(w,wordlist)
            if(hi-lo == 1):
                return w,wordstr[fwl:].lstrip()
            wordlist=wordlist[lo:hi]
        raise Exception("Wordstr %s not found in list" %(w))

    words=[]
    tail=wordstr
    while(len(tail)):
        head,tail=popword(tail,wordlist)
        words.append(head)
    return words

def words_to_mnemonic_int(words,wordlist=wordlist_english):
    if(isinstance(words,str)):
        words=words_split(words,wordlist)
    return sum([wordlist.index(w) << (11*x) for x,w in enumerate(words[::-1])])

def words_verify(words,wordlist=wordlist_english):
    if(isinstance(words,str)):
        words=words_split(words,wordlist)

    mint = words_to_mnemonic_int(words,wordlist)
    mint_bits=len(words)*11
    cs_bits=mint_bits//32
    entropy_bits=mint_bits-cs_bits
    eint=mint >> cs_bits
    csint=mint & ((1 << cs_bits)-1)
    ebytes=_eint_to_bytes(eint,entropy_bits)
    return csint == entropy_cs(ebytes)

def mnemonic_to_seed(mnemonic_phrase,passphrase=''):
    passphrase = from_string_to_bytes(passphrase)
    if isinstance(mnemonic_phrase, (list, tuple)):
        mnemonic_phrase = ' '.join(mnemonic_phrase)
    mnemonic_phrase = from_string_to_bytes(mnemonic_phrase)
    try:
        from hashlib import pbkdf2_hmac
        def pbkdf2_hmac_sha256(password,salt,iters=2048):
            return pbkdf2_hmac(hash_name='sha512',password=password,salt=salt,iterations=iters)
    except:
        try:
            from Crypto.Protocol.KDF import PBKDF2
            from Crypto.Hash import SHA512,HMAC

            def pbkdf2_hmac_sha256(password,salt,iters=2048):
                return PBKDF2(password=password,salt=salt,dkLen=64,count=iters,prf=lambda p,s: HMAC.new(p,s,SHA512).digest())
        except:
            try:

                from pbkdf2 import PBKDF2
                import hmac
                def pbkdf2_hmac_sha256(password,salt,iters=2048):
                    return PBKDF2(password,salt, iterations=iters, macmodule=hmac, digestmodule=hashlib.sha512).read(64)
            except:
                raise RuntimeError("No implementation of pbkdf2 was found!")

    return pbkdf2_hmac_sha256(password=mnemonic_phrase,salt=b'mnemonic'+passphrase)

def words_mine(prefix,entbits,satisfunction,wordlist=wordlist_english,randombits=random.getrandbits):
    prefix_bits=len(prefix)*11
    mine_bits=entbits-prefix_bits
    pint=words_to_mnemonic_int(prefix,wordlist)
    pint<<=mine_bits
    dint=randombits(mine_bits)
    count=0
    while(not satisfunction(entropy_to_words(eint_to_bytes(pint+dint,entbits)))):
        dint=randombits(mine_bits)
        if((count & 0xFFFF) == 0):
            print("Searched %f percent of the space" % (float(count)/float(1 << mine_bits)))

    return entropy_to_words(eint_to_bytes(pint+dint,entbits))

