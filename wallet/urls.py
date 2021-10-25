from django.urls import path, re_path
from . import views
# from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
	#paper wallet
	path('btc/', views.btc_paper_wallet, name='btc-paper-wallet'),
	path('eth/', views.eth_paper_wallet, name='eth-paper-wallet'), 
	path('cache/', views.paper_wallet_cache, name='paper-wallet-cache'),
	# only one qr
	path('one/', views.one_qr, name='one_qr'),	
]