import swagger_client
from swagger_client.rest import ApiException

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.host = "http://174.138.29.231:8070"
configuration.api_key['X-API-KEY'] = 'm5o4u3s2e1-sabo'
walletFilename = 'sabo-trtl-ATM-wallet.wallet'
walletPassword = "m5o4u3s2e1-sabo-ATM"
node = '174.138.29.231'
nodePort = 11898

def setNode():
	api_instance = swagger_client.NodeApi(swagger_client.ApiClient(configuration))
	body = swagger_client.Node() # Node | 
	body.daemon_host = node
	body.daemon_port = nodePort
	try:
		# Sets the node address and port
		api_instance.node_put(body)
	except ApiException as e:
		print("Exception when calling NodeApi->node_put: %s\n" % e)

def openWallet():
	# create an instance of the API class
	setNode()
	api_instance = swagger_client.WalletApi(swagger_client.ApiClient(configuration))
	body = swagger_client.Wallet() # Wallet | 
	body.filename = walletFilename
	body.password = walletPassword
	try:
		# Opens an already existing wallet
		api_instance.wallet_open_post(body)
	except ApiException as e:
		print("Exception when calling WalletApi->wallet_open_post: %s\n" % e)


def getBalance():
	api_instance = swagger_client.BalanceApi(swagger_client.ApiClient(configuration))
	try:
		# Get the balance for the entire wallet container
		api_response = api_instance.balance_get()
		wallet_balance = api_response.unlocked/100
		return wallet_balance
	except ApiException as e:
		print("Exception when calling BalanceApi->balance_get: %s\n" % e)
		return "Error"

def getAddress():

	api_instance = swagger_client.AddressesApi(swagger_client.ApiClient(configuration))
	try:
	# Gets a list of all addresses in the wallet container
		api_response = api_instance.addresses_get()
		wallet_address = api_response.addresses[0]
		return wallet_address
	except ApiException as e:
		print("Exception when calling AddressesApi->addresses_get: %s\n" % e)
		return "Error"

def getWalletStatus():
	api_instance = swagger_client.MiscApi(swagger_client.ApiClient(configuration))
	try:
		# Get the wallet sync status, peer count, and hashrate
		api_response = api_instance.status_get()
		print(api_response)
		return api_response
	except ApiException as e:
		print("Exception when calling MiscApi->status_get: %s\n" % e)

def getWalletKeys():
	address = getAddress()
	api_instance = swagger_client.KeysApi(swagger_client.ApiClient(configuration))

	try:
	# Gets the wallet containers shared private view key
		api_response = api_instance.keys_address_get(address)
		print(api_response)
		return api_response
	except ApiException as e:
		print("Exception when calling KeysApi->keys_get: %s\n" % e)

def getViewKey():
	api_instance = swagger_client.KeysApi(swagger_client.ApiClient(configuration))

	try:
	# Gets the wallet containers shared private view key
		api_response = api_instance.keys_get()
		print(api_response)
		return api_response
	except ApiException as e:
		print("Exception when calling KeysApi->keys_get: %s\n" % e)

def walletAddressValidator(address):
# create an instance of the API class
	api_instance = swagger_client.MiscApi(swagger_client.ApiClient(configuration))
	body = swagger_client.Body1() # Body1 | 
	body.address = address
	try:
	# Validate an address. If the address is valid, a 200 response code will be returned, else a 400 response code will be returned.
		api_response = api_instance.addresses_validate_post(body)
		print(api_response)
#if api_response == 
	except ApiException as e:
		print("Exception when calling MiscApi->addresses_validate_post: %s\n" % e)


def importWallet(private_view_key, private_spend_key):
	pass

def closeWallet():
	pass

def sendTRTL(walletAddress):
	pass


