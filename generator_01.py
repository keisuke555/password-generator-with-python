# 100% Secure Password Generator in Python 3.10 Tutorial (Fast & Easy) 2022
# https://www.youtube.com/watch?v=wNXszxbVU10
import string
import secrets


def generate_password(length: int, symbols: bool, uppercase: bool):
    combination = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_uppercase

    combination_length = len(combination)

    new_password = ""

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password


print(generate_password(length=10, symbols=False, uppercase=True))
