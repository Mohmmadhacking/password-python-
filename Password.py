# password-python-

import random

lower = "abcdefghijklmnopwrstuvwxyz"
upper = "ABCEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
simbols = "!@#$%^&*()_+-=[]{}|;':\",./<>?"

all = lower + upper + number + simbols #combinazioni
length = 10 #lunghezza password

while True:
    password = "".join(random.choices(all, k=length))
    print(password)
