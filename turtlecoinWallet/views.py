from django.shortcuts import render, redirect
from django.http import JsonResponse


from turtlecoinWallet.trtl_wallet_api import getBalance, getAddress, getWalletStatus, getWalletKeys, getViewKey


# Create your views here.


def turtlecoinwallet(request):
	return render(request, 'turtlecoinwallet/trtlATMbackend.html', )


def walletStatus(request):
	status = getWalletStatus()
	statResponse = {
	'hashrate':status.hashrate,
	'local_daemon_block_count' : status.local_daemon_block_count,
	'network_block_count' : status.network_block_count,
	'peer_count' : status.peer_count,
	'sub_wallet_count' : status.sub_wallet_count,
	'wallet_block_count' : status.wallet_block_count
	}
	
	return JsonResponse(statResponse)

def walletKeys(request):
	vkey = getViewKey().private_view_key
	wkeys = getWalletKeys()
	keysResponse = {
	'private_spend_key': wkeys.private_spend_key,
	'public_spend_key': wkeys.public_spend_key,
	'private_view_key':vkey
	}

	return JsonResponse(keysResponse)




#ipn signal handle


	