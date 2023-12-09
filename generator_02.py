# Python tutorial : How to create a random password generator using python for beginners
# https://www.youtube.com/watch?v=qgwEs36D_Xc
import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+|~-=`[]{},./<>?;':\\"

while 1:
    password_len = int(input("What length would you like your password to be? :"))
    password_count = int(input("How many passwords would you like? :"))
    for x in range(0, password_count):
        password = ""
        for x in range(0, password_len):
            password_char = random.choice(chars)
            password += password_char
        print(password)