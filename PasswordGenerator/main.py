#!/bin/python3
import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*ABCDEFGHIJKLMNOPQRSTUVWXYZ'


passwordArray = []

numberOfPassword = input('How many password do you want to make?')
num = int(numberOfPassword)
passwordLength = input('How long do you want the password to be?')
passLength = int(passwordLength)

for num in range(num):
  password = ''
  for length in range(passLength):
    password += random.choice(chars)
  passwordArray.append(password)
print(passwordArray)