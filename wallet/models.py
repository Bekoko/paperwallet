from django.db import models
from django.utils import timezone
from django.conf import settings
import uuid

from django.contrib.auth import get_user_model # If used custom user model

User = get_user_model()

class Private(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
	coin = models.CharField(max_length=150)
	seed = models.CharField(max_length=150)
	priv = models.CharField(max_length=150)
	pub = models.CharField(max_length=150)
	addr = models.CharField(max_length=150)
	xpriv = models.CharField(max_length=150)
	xpub = models.CharField(max_length=150)
	wif = models.CharField(max_length=150)
	seg = models.CharField(max_length=150)
	child = models.CharField(max_length=10000)
	primpub = models.CharField(max_length=150)
	primpriv = models.CharField(max_length=150)

	time = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return str(self.time.strftime('%m-%d-%Y, %H-%M %p'))
		

# Create your models here.
class BTC_PW(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
	coin = models.CharField(max_length=30, blank=True, null=True)
	address = models.CharField(max_length=50)
	time = models.DateTimeField(default=timezone.now)
	
	user = models.ForeignKey(User, blank=True, 
		null=True, on_delete=models.PROTECT)

	def __str__(self):
		return str(self.time.strftime('%m-%d-%Y, %H-%M %p'))


class ETH_PW (models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
	coin = models.CharField(max_length=30, blank=True, null=True)
	address = models.CharField(max_length=50)
	time = models.DateTimeField(default=timezone.now)
	
	user = models.ForeignKey(User, blank=True, 
		null=True, on_delete=models.PROTECT)

	def __str__(self):
		return str(self.time.strftime('%m-%d-%Y, %H-%M %p'))


class LTC_PW(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
	coin = models.CharField(max_length=30, blank=True, null=True)
	address = models.CharField(max_length=50)
	time = models.DateTimeField(default=timezone.now)
	
	user = models.ForeignKey(User, blank=True, 
		null=True, on_delete=models.PROTECT)


	def __str__(self):
		return str(self.time.strftime('%m-%d-%Y, %H-%M %p'))


class BCH_PW(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
	coin = models.CharField(max_length=30, blank=True, null=True)
	address = models.CharField(max_length=50)
	time = models.DateTimeField(default=timezone.now)
	
	user = models.ForeignKey(User, blank=True, 
		null=True, on_delete=models.PROTECT)

	def __str__(self):
		return str(self.time.strftime('%m-%d-%Y, %H-%M %p'))


class DOGE_PW(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
	coin = models.CharField(max_length=30, blank=True, null=True)
	address = models.CharField(max_length=50)
	time = models.DateTimeField(default=timezone.now)
	
	user = models.ForeignKey(User, blank=True, 
		null=True, on_delete=models.PROTECT)

	def __str__(self):
		return str(self.time.strftime('%m-%d-%Y, %H-%M %p'))


class ATOM_PW(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
	coin = models.CharField(max_length=30, blank=True, null=True)
	address = models.CharField(max_length=50)
	time = models.DateTimeField(default=timezone.now)
	
	user = models.ForeignKey(User, blank=True, 
		null=True, on_delete=models.PROTECT)

	def __str__(self):
		return str(self.time.strftime('%m-%d-%Y, %H-%M %p'))


class EOS_PW(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
	coin = models.CharField(max_length=30, blank=True, null=True)
	address = models.CharField(max_length=50)
	time = models.DateTimeField(default=timezone.now)
	
	user = models.ForeignKey(User, blank=True, 
		null=True, on_delete=models.PROTECT)

	def __str__(self):
		return str(self.time.strftime('%m-%d-%Y, %H-%M %p'))


