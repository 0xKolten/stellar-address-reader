from stellar_base.address import Address
import requests
import json

# Get data market data from Stellar ticker
r = requests.get('https://ticker.stellar.org/markets.json')
json_obj = r.json()

# Parse through market data for XLM_USD pair - has most volume
def get_price(json_obj, name):
    for dict in json_obj['pairs']:
              if dict['name'] == name:
                  return dict['price']

# Set XLM price in USD ( $1 / # XLM ) 
xlm_price =  1 / get_price(json_obj, 'XLM_USD') 

# Start 
print ()
pub_key = input("Input public key: ")

# Store address data in address variable
address = Address(address=pub_key, secret=None, network='public')

# Get information from Horizon
address.get()

# Store XLM balance and convert to float 
xlm_balance = float(address.balances[-1]['balance']) # XLM is always listed last in address.balances 

# Print XLM balance and USD equivalent 
print('\nCurrent XLM Balance: ' + str(xlm_balance) + ' XLM' + ' (~$' + str(xlm_price*xlm_balance) + ')')

