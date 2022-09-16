from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError
import dict_digger

def ppfunc():
	cmc = CoinMarketCapAPI('056f35b8-8202-4f3d-9437-34a590466b2b')

	try:
		r = cmc.cryptocurrency_info(symbol='BTC')
	except CoinMarketCapAPIError as e:
		r = e.rep
	
	# print(repr(r.error))
	# print(repr(r.status))
	# print(repr(r.data))
	# print(dict_digger.dig(r.data, 'BTC', 'description'))

	my_string = dict_digger.dig(r.data, 'BTC', 'description')

	counter = 0

	clean_string = ""

	for element in my_string:
		if element == ".":
			counter = counter + 1
		if counter == 3:
			clean_string += element
		
	print(clean_string)
	return clean_string
