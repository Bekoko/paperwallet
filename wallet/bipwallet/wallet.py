from datetime import datetime
from .utils import (
    Wallet, 
    HDPrivateKey, 
    HDKey, 
)
from .utils.utils import checksummed
from .network import *
import inspect



def get_network(network='btctest'):
    network = network.lower()

    if network == "bitcoin_testnet" or network == "btctest":
        return BitcoinTestNet
    elif network == "bitcoin" or network == "btc":
        return BitcoinMainNet
    elif network == "dogecoin" or network == "doge":
        return DogecoinMainNet
    elif network == "dogecoin_testnet" or network == "dogetest":
        return DogecoinTestNet
    elif network == "litecoin" or network == "ltc":
        return LitecoinMainNet
    elif network == "litecoin_testnet" or network == "ltctest":
        return LitecoinTestNet
    elif network == "bitcoin_cash" or network == "bch":
        return BitcoinCashMainNet
    elif network == "bitcoin_gold" or network == "btg":
        return BitcoinGoldMainNet
    elif network == "dash":
        return DashMainNet
    elif network == "dash_testnet" or network == 'dashtest':
        return DashTestNet
    elif network == 'omni':
        return OmniMainNet
    elif network == 'omni_testnet':
        return OmniTestNet
    elif network == "feathercoin" or network == 'ftc':
        return FeathercoinMainNet
    elif network == "qtum":
        return QtumMainNet
    elif network == "qtum_testnet" or network == "qtumtest":
        return QtumTestNet

    return BitcoinTestNet


def generate_mnemonic(strength=128):
    _, seed = HDPrivateKey.master_key_from_entropy(strength=strength)
    return seed


def generate_child_id():
    now = datetime.now()
    seconds_since_midnight = (now - now.replace(
        hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    return int((int(now.strftime(
        '%y%m%d')) + seconds_since_midnight*1000000) // 100)


def create_address(network='btctest', xpriv=None, xpub=None, child=None, path=0):
    if xpub:
        assert xpub is not None
    else:
        assert xpriv is not None

    if child is None: 
        child = generate_child_id()

    if network == 'ethereum' or network.upper() == 'ETH':
        acct_key = HDKey.from_b58check(xpriv or xpub)
        keys = HDKey.from_path(
            acct_key, '{change}/{index}'.format(
                                                change=path,
                                                index=child
                                            )
        )
        if xpriv:
            res = {
                "path": "m/" + str(acct_key.index) + "/" + str(keys[-1].index),
                "bip32_path": "m/44'/60'/0'/" + str(acct_key.index) + "/" + str(keys[-1].index),
                "address": checksummed(keys[-1].public_key.address())
            }
            # if inspect.stack()[1][3] == "create_wallet":
            res["xpublic_key"] = keys[-1].to_b58check()
            res["xprivate_key"] = keys[-1].to_b58check()
            res["public_key"] = acct_key.to_hex()
            res["private_key"] = keys[-1].to_hex()
            return res
        else:
            res = {
                "path": "m/" + str(acct_key.index) + "/" + str(keys[-1].index),
                "bip32_path": "m/44'/60'/0'/" + str(acct_key.index) + "/" + str(keys[-1].index),
                "address": checksummed(keys[-1].address())
            }
            # if inspect.stack()[1][3] == "create_wallet":
            res["xpublic_key"] = keys[-1].to_b58check()
            res["public_key"] = acct_key.to_hex()
            return res
    # else ...
    wallet_obj = Wallet.deserialize(
                                xpriv or xpub, 
                                network=network.upper()
                            )
    if xpriv:
        child_wallet = wallet_obj.get_child(child, is_prime=False, as_private=True)
    else:
        child_wallet = wallet_obj.get_child(child, is_prime=False, as_private=False)

    net = get_network(network)

    if xpriv:
        return {
            "path": "m/" + str(wallet_obj.child_number) + "/" +str(child_wallet.child_number),
            "bip32_path": net.BIP32_PATH + str(wallet_obj.child_number) + "/" +str(child_wallet.child_number),
            "address": child_wallet.to_address(),
            "segwit": child_wallet.to_segwit_address(),
            "private_key": child_wallet.private_key.get_key().decode(),
            "public_key": child_wallet.public_key.get_key().decode(),
            "xpublic_key": child_wallet.serialize_b58(private=False),
            "xprivate_key": child_wallet.serialize_b58(private=True),
            "wif": child_wallet.export_to_wif(), # needs private key
            "xpublic_key_prime": child_wallet.serialize_b58(private=False),
            "xprivate_key_prime": child_wallet.serialize_b58(private=True),
        }
    else:
        return {
            "path": "m/" + str(wallet_obj.child_number) + "/" +str(child_wallet.child_number),
            "bip32_path": net.BIP32_PATH + str(wallet_obj.child_number) + "/" +str(child_wallet.child_number),
            "address": child_wallet.to_address(),
            "segwit": child_wallet.to_segwit_address(),
            "public_key": child_wallet.public_key.get_key().decode(),
            "xpublic_key": child_wallet.serialize_b58(private=False),
            "xpublic_key_prime": child_wallet.serialize_b58(private=False),
        }




def create_wallet(network='btctest', seed=None, children=1):
    if seed is None:
        seed = generate_mnemonic()

    net = get_network(network)
    wallet = {
        "coin": net.COIN,
        "seed": seed,
        "private_key": "",
        "public_key": "",
        "xprivate_key": "",
        "xpublic_key": "",
        "address": "",
        "wif": "",
        "children": []
    }

    if network == 'ethereum' or network.upper() == 'ETH':
        wallet["coin"] = "ETH"

        master_key = HDPrivateKey.master_key_from_mnemonic(seed)
        root_keys = HDKey.from_path(master_key, "m/44'/60'/0'")

        acct_priv_key = root_keys[-1]
        acct_pub_key = acct_priv_key.public_key

        # print(master_key, root_keys[0].to_hex(), acct_priv_key, acct_pub_key)

        # wallet["private_key"] = acct_priv_key.to_hex()
        wallet["private_key"] = acct_priv_key._key.to_hex()
        wallet["public_key"] = acct_pub_key.to_hex()
        wallet["xprivate_key"] = acct_priv_key.to_b58check()
        wallet["xpublic_key"] = acct_pub_key.to_b58check()

        child_wallet = create_address(
                                    network=network.upper(), 
                                    xpriv=wallet["xprivate_key"],
                                    child=0, 
                                    path=0
                                )
        # 这个地址是私钥的
        wallet["address"] = checksummed(acct_priv_key.public_key.address())
        # 这个地址是助记词的
        wallet["seed_address"] = child_wallet["address"]
        # get public info from first prime child
        for child in range(children):
            print(child_wallet)
            child_wallet = create_address(
                                        network=network.upper(), 
                                        xpriv=wallet["xprivate_key"],
                                        child=child, 
                                        path=0
                                    )
            wallet["children"].append({
                "address": checksummed(child_wallet["address"]),
                "public_key": child_wallet["public_key"],
                "private_key": child_wallet["private_key"],
                "xpublic_key": child_wallet["xpublic_key"],
                "xprivate_key": child_wallet["xprivate_key"],
                "path": "m/" + str(child),
                "bip32_path": "m/44'/60'/0'/" + str(child),
            })
    else:
        my_wallet = Wallet.from_master_secret(
                                        network=network.upper(), 
                                        seed=seed
                                    )
        # account level
        wallet["private_key"] = my_wallet.private_key.get_key().decode()
        wallet["public_key"] = my_wallet.public_key.get_key().decode()
        wallet["xprivate_key"] = my_wallet.serialize_b58(private=True)
        wallet["xpublic_key"] = my_wallet.serialize_b58(private=False)
        wallet["address"] = my_wallet.to_address()
        wallet["segwit"] = my_wallet.to_segwit_address()
        wallet["wif"] = my_wallet.export_to_wif(),
        prime_child_wallet = my_wallet.get_child(0, is_prime=True)
        wallet["xpublic_key_prime"] = prime_child_wallet.serialize_b58(private=False)
        wallet["xprivate_key_prime"] = prime_child_wallet.serialize_b58(private=True)
        # prime children
        for child in range(children):
            child_wallet = my_wallet.get_child(child, is_prime=False, as_private=True)
            wallet["children"].append({
                "private_key": child_wallet.private_key.get_key().decode(),
                "public_key": child_wallet.public_key.get_key().decode(),
                "xpublic_key": child_wallet.serialize_b58(private=False),
                "xprivate_key": child_wallet.serialize_b58(private=True),
                "address": child_wallet.to_address(),
                "segwit": child_wallet.to_segwit_address(),
                "wif": child_wallet.export_to_wif(),
                "path": "m/" + str(child),
                "bip32_path": net.BIP32_PATH + str(child_wallet.child_number),
                "xpublic_key_prime": child_wallet.serialize_b58(private=False),
                "xprivate_key_prime": child_wallet.serialize_b58(private=True),
            })

    return wallet