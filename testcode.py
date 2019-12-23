"""
# !/usr/bin/env python
"""

import math
import sys
from os import rename

import requests


print(sys.version)
# print(sys.executable)
def greet(who):
    greeting = "Hello, {}!".format(who)
    return greeting


person_b = "John Adams"
print(person_b)
print(greet("Walter"))
r = requests.get("https://coreyms.com")
print(r.status_code)

# name = input("Your Name: ")
# print("Hello, ", name)
