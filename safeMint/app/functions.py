# command to run in bash/cmd:
# python3.exe functions.py

from coinbase.wallet.client import Client
import sys
import datetime

# The client element will use our API that we have for coinbase.com, ricky created
# an account and got an API key. It queries coinbase's server for the price of
# currency_from/currency_to divisor.
# It uses the API from:
# developers.coinbase.com/docs/wallet/guides/price-data
# to get data on cryptocurrencies
client = Client("CqUy59ynpeYzRwXN", "ECGuB2sH7xYcuq1mDXt2IvANWxXECH8U", api_version='2018-04-02')

# Reading the file given from the arg
def readFile(f):
	with open(fname) as f:
		content = f.readlines()
	for line in content:
		print(line)

# print command line arguments
def main():
	# account creation:
	# [date bought, crypto name, amount bought, currency to display in]
	accounts  = []
	accounts += [("2017-12-20", "BTC", 1.2, "USD")]
	accounts += [("2017-12-20", "ETH", 90.0, "USD")]
	accounts += [("2014-09-20", "BTC", 90.0, "CAD")]
	accounts += [("2016-02-01", "BTC", 100.1, "USD")]
	# print(accounts)

	for x in accounts:
		# the main function is coinbase.get_spot_price(). Will return c1/c2
		# double precision. Documentation can be read at:
		# https://github.com/coinbase/coinbase-python
		# Also, you need to feed 'c1-c2' into get_spot_price(), but you shouldn't
		# convert from physical currency to cryptocurrency. No 'USD-BTC' or 'USD-ETH'
		past_conversion_rate = client.get_spot_price(currency_pair = (x[1] + '-' + x[3]), date=x[0]).amount
		current_conversion_rate = client.get_spot_price(currency_pair = (x[1] + '-' + x[3])).amount
		print('You bought {} {} on {}. Good job.'.format(x[2], x[1], x[0]))
		print('It cost {} {} for one {} when you bought it on {}.'.format(past_conversion_rate, x[3], x[1], x[0]))
		print('You paid {:.2f} {} for it.'.format(float(past_conversion_rate)*x[2], x[3]))
		print('Now it costs {} {} for one {}. You now have {:.2f} {}.'.format(current_conversion_rate, x[3], x[1], float(current_conversion_rate)*x[2], x[3]))
		input("Press Enter to continue...")
		print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

if __name__ == "__main__":
	main()