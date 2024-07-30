#How to use f-string

name=input("What's your name? ")
print(f"Hello {name}")

import math
print(f"Your num {math.pi:.3f}")

num=15
print(f"My number is {num:05d}")

import datetime
today=datetime.datetime.today()
print(f"{today:%b %d, %y}")