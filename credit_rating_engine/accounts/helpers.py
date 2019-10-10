import hashlib
import string
import random

#nin - CF89048107KMED
def hash_input(input):
    return hashlib.sha256(input.encode()).hexdigest()

#generate random user number
def random_string_digits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_uppercase + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))





