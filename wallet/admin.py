from django.contrib import admin
from .models import (
	BTC_PW,
	ETH_PW,
	LTC_PW,
	BCH_PW,
	DOGE_PW,
	ATOM_PW,
	EOS_PW,
	Private,
)

# Register your models here.
admin.site.register(Private)

# admin.site.register(BTC_PW)
# admin.site.register(ETH_PW)
# admin.site.register(LTC_PW)
# admin.site.register(BCH_PW)
# admin.site.register(DOGE_PW)
# admin.site.register(ATOM_PW)
# admin.site.register(EOS_PW)