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

file_ = open(os.path.join(settings.BASE_DIR, 'loans/test.txt'))

class CreditRator:
    def __init__(self):
        pass

    def sum_all_criteria(self):
        pass

#nin - CF89048107KMED
def hash_input(input):
    return hashlib.sha256(input.encode()).hexdigest()

#generate random user number
def random_string_digits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_uppercase + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

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
        url="https://{}/api/node/bms.php".format(peer)
        headers={'content-type': 'multipart/form-data'}
    
        r = requests.request('POST', url, 
            files={'name': open(file_, 'r'), 'method':'createWallet',
            'currency':5,
            'api_key':'FAD7EE3DE4CB65F62C882038516A9C5F976BB70BCE688FD6854A70DF159142D4',
            'wallet':'01016'
        }).prepare()
        print(r.status_code)
        print(r.text)
        return r.json().get('address')






    