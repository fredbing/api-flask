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


print(greet("John"))
r = requests.get("https://coreyms.com")
print(r.status_code)

# name = input("Your Name: ")
# print("Hello, ", name)
