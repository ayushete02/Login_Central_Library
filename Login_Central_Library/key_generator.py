import string
import random


s1 = string.ascii_letters
s2 = string.digits
# s3 = string.punctuation

s = []
# extend is same as apend bt apend direct put main file to other bt extend put element to another
s.extend(list(s1))
s.extend(list(s2))

random.shuffle(s)

def Random_Number1():
    return ("".join(s[0:5]))



