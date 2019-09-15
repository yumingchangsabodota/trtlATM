from django.db import models

# Create your models here.

from django.contrib import admin
from datetime import datetime
import uuid
from turtlecoinWallet.trtl_wallet_api import walletAddressValidator

# Create your models here.
class TRTLOrder(models.Model):
	sendToWallet = models.CharField(max_length=100)
	amountInTRTL = models.DecimalField(max_digits=5, decimal_places=2)
	amountInUSD = models.DecimalField(max_digits=5, decimal_places=2)
	nickname = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	paid = models.BooleanField(default=False)
	trtlsent = models.BooleanField(default=False)
	tx = models.CharField(max_length=100, default='NA')

	class Meta:
		ordering = ('-created',)

	def __str__(self): 
		return 'Order {}'.format(self.id)  #entry name displayed in admin site



class TRTLOrderAdmin(admin.ModelAdmin):
    list_display = ['id','sendToWallet','amountInTRTL','amountInUSD',
    				'nickname','created','updated', 'paid', 'trtlsent', 'tx' ]  #entry name displayed in admin site


def is_valid_trtlOrder(trtlamount):

	if trtlamount < 2:

		return False
	else:
		return True