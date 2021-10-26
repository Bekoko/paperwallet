from django.shortcuts import render
from .utils import *
from .models import *
from .bipwallet import wallet
from .forms import *
#pdf
from django.template.loader import get_template
from .utils import *
from django.core.files import File
from io import BytesIO
# downloadable
from wsgiref.util import FileWrapper
import mimetypes
from pdf2image import convert_from_path
# btc and eth libs to verify 
from wallet.cryptos import *
from eth_account import Account

def one_qr(request):
	priv = None
	form = OneQrCodeForm(request.POST or None)	
	if form.is_valid():
		priv = form.cleaned_data.get('priv')
	context = {
		'form':form,
		'priv':priv,
	}	
	return render(request, 'wallet/one.html', context)


def btc_paper_wallet(request):
	_list = []
	_list = create_btc_pw(request)
	for w in _list:

		priv = w['private_key'] 
		addr = w['address']

		# assert that each priv key corespond to addr
		try:
			assert Bitcoin().privtoaddr(priv) == addr

			# c = BTC_PW.objects.create(coin="BTC", address=addr)
			# c.save()			

		except:
			print("error")
			_list.remove(w)


	context = {
		'_list':_list,

		'address__1': (_list[0]).get('address'),
		'private__1': (_list[0]).get('private_key'),
		
		'address__2': (_list[1]).get('address'),
		'private__2': (_list[1]).get('private_key'),
		
		'address__3': (_list[2]).get('address'),
		'private__3': (_list[2]).get('private_key'),
		
		'address__4': (_list[3]).get('address'),
		'private__4': (_list[3]).get('private_key'),
		
		'address__5': (_list[4]).get('address'),
		'private__5': (_list[4]).get('private_key'),
		
		'address__6': (_list[5]).get('address'),
		'private__6': (_list[5]).get('private_key'),
		
		'address__7': (_list[6]).get('address'),
		'private__7': (_list[6]).get('private_key'),
		
		'address__8': (_list[7]).get('address'),
		'private__8': (_list[7]).get('private_key'),
		
		'address__9': (_list[8]).get('address'),
		'private__9': (_list[8]).get('private_key'),
		
		'address__10': (_list[9]).get('address'),
		'private__10': (_list[9]).get('private_key'),
		
		'address__11': (_list[10]).get('address'),
		'private__11': (_list[10]).get('private_key'),
		
		'address__12': (_list[11]).get('address'),
		'private__12': (_list[11]).get('private_key'),

		'address__13': (_list[12]).get('address'),
		'private__13': (_list[12]).get('private_key'),
		
		'address__14': (_list[13]).get('address'),
		'private__14': (_list[13]).get('private_key'),
		
		'address__15': (_list[14]).get('address'),
		'private__15': (_list[14]).get('private_key'),
		
		'address__16': (_list[15]).get('address'),
		'private__16': (_list[15]).get('private_key'),
		
		'address__17': (_list[16]).get('address'),
		'private__17': (_list[16]).get('private_key'),
		
		'address__18': (_list[17]).get('address'),
		'private__18': (_list[17]).get('private_key'),

		'address__19': (_list[18]).get('address'),
		'private__19': (_list[18]).get('private_key'),
		
		'address__20': (_list[19]).get('address'),
		'private__20': (_list[19]).get('private_key'),
		
		'address__21': (_list[20]).get('address'),
		'private__21': (_list[20]).get('private_key'),
		
		'address__22': (_list[21]).get('address'),
		'private__22': (_list[21]).get('private_key'),
		
		'address__23': (_list[22]).get('address'),
		'private__23': (_list[22]).get('private_key'),	

		'address__24': (_list[23]).get('address'),
		'private__24': (_list[23]).get('private_key'),			
		
	}

	return render(request, 'wallet/qr_codes.html', context)


def eth_paper_wallet(request):
	_list = []
	_list = create_eth_pw(request)
	for w in _list:
		priv = w['private_key'] 
		addr = w['address']

		# assert that each priv key corespond to addr
		try:

			acct = Account.from_key(priv)

			assert acct.address == addr

			# c = ETH_PW.objects.create(coin="ETH", address=addr)
			# c.save()			

		except:
			print("error")
			_list.remove(w)


	context = {
		'_list':_list,

		'address__1': (_list[0]).get('address'),
		'private__1': (_list[0]).get('private_key'),
		
		'address__2': (_list[1]).get('address'),
		'private__2': (_list[1]).get('private_key'),
		
		'address__3': (_list[2]).get('address'),
		'private__3': (_list[2]).get('private_key'),
		
		'address__4': (_list[3]).get('address'),
		'private__4': (_list[3]).get('private_key'),
		
		'address__5': (_list[4]).get('address'),
		'private__5': (_list[4]).get('private_key'),
		
		'address__6': (_list[5]).get('address'),
		'private__6': (_list[5]).get('private_key'),
		
		'address__7': (_list[6]).get('address'),
		'private__7': (_list[6]).get('private_key'),
		
		'address__8': (_list[7]).get('address'),
		'private__8': (_list[7]).get('private_key'),
		
		'address__9': (_list[8]).get('address'),
		'private__9': (_list[8]).get('private_key'),
		
		'address__10': (_list[9]).get('address'),
		'private__10': (_list[9]).get('private_key'),
		
		'address__11': (_list[10]).get('address'),
		'private__11': (_list[10]).get('private_key'),
		
		'address__12': (_list[11]).get('address'),
		'private__12': (_list[11]).get('private_key'),

		'address__13': (_list[12]).get('address'),
		'private__13': (_list[12]).get('private_key'),
		
		'address__14': (_list[13]).get('address'),
		'private__14': (_list[13]).get('private_key'),
		
		'address__15': (_list[14]).get('address'),
		'private__15': (_list[14]).get('private_key'),
		
		'address__16': (_list[15]).get('address'),
		'private__16': (_list[15]).get('private_key'),
		
		'address__17': (_list[16]).get('address'),
		'private__17': (_list[16]).get('private_key'),
		
		'address__18': (_list[17]).get('address'),
		'private__18': (_list[17]).get('private_key'),

		'address__19': (_list[18]).get('address'),
		'private__19': (_list[18]).get('private_key'),
		
		'address__20': (_list[19]).get('address'),
		'private__20': (_list[19]).get('private_key'),
		
		'address__21': (_list[20]).get('address'),
		'private__21': (_list[20]).get('private_key'),
		
		'address__22': (_list[21]).get('address'),
		'private__22': (_list[21]).get('private_key'),
		
		'address__23': (_list[22]).get('address'),
		'private__23': (_list[22]).get('private_key'),	

		'address__24': (_list[23]).get('address'),
		'private__24': (_list[23]).get('private_key'),			
		
	}

	return render(request, 'wallet/qr_codes.html', context)


def paper_wallet_cache(request):
	context = {}
	return render(request, 'wallet/paper_wallet_cache.html', context)

