# command to run in bash/cmd:
# python3.exe functions.py

from coinbase.wallet.client import Client
import sys

# this function will use our API that we have for coinbase.com, ricky created
# an account and got an API key. It queries coinbase's server for the price of
# currency_from/currency_to divisor.
# It uses the API from:
# developers.coinbase.com/docs/wallet/guides/price-data
# to get data on cryptocurrencies
def get_price_from_coinbase(date, currency_from, currency_to):
	client = Client("CqUy59ynpeYzRwXN", "ECGuB2sH7xYcuq1mDXt2IvANWxXECH8U", api_version='2018-04-02')

	# the main function is coinbase.get_spot_price(c1, c2). Will return c1/c2
	# in double precision. Documentation can be read at:
	# https://github.com/coinbase/coinbase-python
	# Also, you need to feed 'c1-c2' into get_spot_price(), but you shouldn't
	# convert from smaller value to bigger value. No 'USD-BTC'
	# print('Current bitcoin price in {}/{} = {}'.format(currency_from, currency_to, client.get_spot_price(currency_pair = (currency_from + '-' + currency_to), date='2017-12-20').amount))
	return client.get_spot_price(currency_pair = (currency_from + '-' + currency_to), date='2017-12-20').amount

# Reading the file given from the arg
def readFile(f):
	with open(fname) as f:
		content = f.readlines()
	for line in content:
		print(line)

# print command line arguments
def main():
	# print('hello')
	print('price at \'{}\''.format(get_price_from_coinbase("2017-12-20", "BTC", "USD")))
	# get_price_from_coinbase(2018, "USD", "USD")

	# print command line arguments
	# for arg in sys.argv[1:]:
	# 	print(arg)              #The file you want to read
	# 	readFile(arg)           #Reading the file with the readFile() method

if __name__ == "__main__":
	main()