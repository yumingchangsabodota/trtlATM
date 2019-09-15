from django.shortcuts import render

from .market_price_api import get_market_price

from turtlecoinWallet.trtl_wallet_api import getBalance, getAddress, getWalletStatus, getWalletKeys, getViewKey, openWallet, walletAddressValidator

# Create your views here.
def home(request):

	price = get_market_price('turtlecoin')
	price = format(price,'.8f')

	wallet_address = getAddress()

	if wallet_address == 'Error':
		openWallet()

	wallet_address = getAddress()
	wallet_balance = getBalance()
	getWalletStatus()
	getWalletKeys()

	return render(request, 'home.html', {'price':price, 'wallet_balance':wallet_balance, 'wallet_address':wallet_address})