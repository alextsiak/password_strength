'''
password_strength.py - Identifies strength of passwords.
'''

import re

lengthRegex = re.compile(r'\w{8,}')
upperRegex = re.compile(r'[A-Z]+')
lowerRegex = re.compile(r'[a-z]+')
digitRegex = re.compile(r'\d+')

password = input("Enter your password: ")

mo = lengthRegex.search(password)
mo2 = upperRegex.search(password)
mo3 = lowerRegex.search(password)
mo4 = digitRegex.search(password)

if mo != None and mo2 != None and mo3 != None and mo4 != None:
    print("Congratulations! Your password is strong.")
else:
    print("Your password is weak and so are you.")
