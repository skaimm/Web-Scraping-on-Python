# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 17:07:34 2020

@author: uasmt
"""

import requests
import json

api_url = "https://api.exchangeratesapi.io/latest?base="



while True:
    w_currency = input("currency you want to change : ").upper()
    result = requests.get(api_url+w_currency)
    result = json.loads(result.text)
    
    try:
        print(result["rates"])
    except KeyError:
        print('Currency is wrong ')
        break
    
    e_currency = input(f"{w_currency}  to : ").upper()
    
    try:
        result["rates"][e_currency]
    except KeyError:
        print('Currency is wrong ')
        break
    
    print("1 {0} = {1} {2}".format(w_currency,result["rates"][e_currency],e_currency))
    
    quantity = int(input("How much money you want to exchange {w_currency} to {e_currency}: "))
    
    print("{0} {1} = {2} {3}".format(quantity,w_currency,quantity*result["rates"][e_currency],e_currency))
    result