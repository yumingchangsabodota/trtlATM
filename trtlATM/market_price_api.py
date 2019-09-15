from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()

def get_market_price(symbol_id):
	try:
		price = cg.get_price(ids= symbol_id, vs_currencies='usd')['turtlecoin']['usd']
	except Exception as e:
		print(e)
		price = 123

	return price
	

#below uses the private coinmarketcap API, but it has limited request per day,
#use coingecko for now
'''
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
my_api = '64481a08-414f-473b-b488-5b6fb27098ea'

def get_market_price(symbol_id):

	parameters = {
	  'id':str(symbol_id)
	}
	headers = {
	  'Accepts': 'application/json',
	  'X-CMC_PRO_API_KEY': my_api,
	}

	session = Session()
	session.headers.update(headers)

	try:
	  response = session.get(url, params=parameters)
	  data = json.loads(response.text)
	  #print(data)
	  
	  return data['data'][str(symbol_id)]['quote']['USD']['price']
	except (ConnectionError, Timeout, TooManyRedirects) as e:
	  print(e)

def get_symbol_id(symbol):
	parameters = {
	  'symbol':symbol
	}
	headers = {
	  'Accepts': 'application/json',
	  'X-CMC_PRO_API_KEY': my_api,
	}
	session = Session()
	session.headers.update(headers)

	try:
	  response = session.get(url, params=parameters)
	  data = json.loads(response.text)
	  #print(data)
	  symbol_id = data['data'][symbol]['id']
	  return symbol_id
	except (ConnectionError, Timeout, TooManyRedirects) as e:
	  print(e)
'''
