from django.forms import ModelForm
from .models import Private
from django import forms


class WalletForm(ModelForm):
    coin = forms.CharField(
        label='Coin',
    )
    class Meta:
        model = Private
        fields = [
            'coin',
        ]



class PdfToJpgForm(forms.Form):
    file = forms.FileField()


class OneQrCodeForm(forms.Form):
    priv = forms.CharField(
        label='PrivateKey',
    )

