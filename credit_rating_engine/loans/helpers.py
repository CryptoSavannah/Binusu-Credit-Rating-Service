"""
Author: Allan Katongole
Date: 17th September 2019
Purpose: Helper classes for the Binusu Credit Rating Service
"""
import hashlib
import string
import random
import requests
from .models import Loans, LoanPayments
import os
from django.conf import settings

class CreditRator:
    def __init__(self):
        pass

    def sum_all_criteria(self):
        pass

    def credit_refferal_score(self, creditor):
        if creditor.refferal_id == None:
            return 80

#get bnu_address
class BnuAddressCollector:
    def __init__(self):
        self.__params = {
            "node":"https://explorer.binusu.com/get_peer_list/index.php"
        }
    
    def get_node(self):
        headers={'User-Agent': "bincred_client"}
        r = requests.request("GET", self.__params.get('node'), headers=headers)
        if r.status_code==200:
            self.__params.update({"node":r.json().get('peer')})
            return r.json().get('peer')
        else:
            print("failed bitch")

    def get_bnu_address(self, peer):
        url="https://{}/api/node/mobile_api.php".format(peer)
        headers={'Content-Type': 'application/json'}
    
        r = requests.request('POST', url, data={
            'method':'createMobileWallet',
        })
        print(r.json())
        response = r.json().get('response')
        return [response.get('address'), response.get('spendSecretKey'), response.get('spendPublicKey')]






    