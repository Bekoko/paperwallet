
#BTC, BTG, BCH, ETH, LTC, DASH, DOGE -> YES:
from .bipwallet import wallet
#EOS -> NONE-YES:
# https://eosio.stackexchange.com/questions/1179/how-will-someone-new-to-eos-create-an-eos-account-today
# from eosjs_python import Eos
import json
import requests
#ATOM -> YES:
# from cosmospy import generate_wallet
#ADA -> NONE on dedicated ADA blockchain
#GNO -> NONE but interactable via Python (https://pypi.org/project/gnosis-py/) // on ETH blockchain as ERC20
#ICX -> None but but package ok and moduls exist (https://github.com/icon-project/icon_sdk_for_python)
	# from iconsdk.icon_service import IconService
	# import iconsdk
#NANO -> NONE (https://docs.nano.org/commands/rpc-protocol/ ) // on dedicated blckchain
#TRON -> NONE(https://developers.tron.network/docs/tron-wallet-rpc-api) // on dedicated blochain
#MLN -> ERC-20 (https://melonprotocol.com/)
#DAI -> ERC-20 (https://kauri.io/quick-guide-integrating-dai-or-mkr-tokens-in-wallets/10158e201b024ffe99389879da006599/a)
#OMG -> ERC-20
#REP -> ERC-20
#LINK -> ERC-20
#QTUM -> NONE //on dedicated blockchain
#SC -> ERC-20
#USDT -> ERC-20
#TRX -> NONE -> on dedicated blchchain (https://tronpaperwallet.org/)
#WAIVES -> NONE // dedicated blockchain (https://github.com/wavesplatform/WavesGUI)
#XLP -> NONE (no info)
#XRP -> NONE / on dedicated wallet in python : (https://github.com/devrandom/pymultiwallet) (https://github.com/stevenzeiler/ripple-wallet) (https://tezos.stackexchange.com/questions/1438/tezos-wallet-addresses-generation)
#BSV _> NONE (no info)

from .bipwallet import wallet
import secrets
from wallet.cryptos import *
from eth_account import Account


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++1
# wallets

def create_btc_pw(request):
	x = range(24)
	btc_list = []
	for i in x:
		# seed = wallet.generate_mnemonic()
		# w = wallet.create_wallet(network="BTC", seed=seed, children=0)
		n = secrets.randbits(255)
		priv = sha256(str(n))
		addr = Bitcoin().privtoaddr(priv)
		print(n,priv,addr)						
		btc_list.append({"address":addr,"private_key":priv})

	return btc_list

def create_eth_pw(request):
	x = range(24)
	eth_list = []
	for i in x:
		seed = wallet.generate_mnemonic()
		w = wallet.create_wallet(network="ETH", seed=seed, children=0)
		eth_list.append(w)

	return eth_list

def create_ltc_pw(request):
	x = range(18)
	ltc_list = []
	for i in x:
		seed = wallet.generate_mnemonic()
		w = wallet.create_wallet(network="LTC", seed=seed, children=0)
		ltc_list.append(w)

	return ltc_list

def create_bch_pw(request):
	x = range(18)
	bch_list = []
	for i in x:
		seed = wallet.generate_mnemonic()
		w = wallet.create_wallet(network="BCH", seed=seed, children=0)
		bch_list.append(w)

	return bch_list

def create_doge_pw(request):
	x = range(18)
	doge_list = []
	for i in x:
		seed = wallet.generate_mnemonic()
		w = wallet.create_wallet(network="DOGE", seed=seed, children=0)
		doge_list.append(w)

	return doge_list

def create_atom_pw(request):
	x = range(18)
	atom_list = []
	for i in x:
		w = generate_wallet()
		atom_list.append(w)

	return atom_list

def create_eos_pw(request):
	x = range(18)
	eos_list = []
	for i in x:
		w = Eos.generate_key_pair()
		eos_list.append(w)

	return eos_list

