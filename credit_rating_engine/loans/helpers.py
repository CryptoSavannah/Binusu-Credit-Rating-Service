"""
Author: Allan Katongole
Date: 17th September 2019
Purpose: Helper classes for the Binusu Credit Rating Service
"""
import hashlib
import string
import random
from .models import Loans, LoanPayments

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

    