# Mini Python Project Tutorial - Password Generator
# https://www.youtube.com/watch?v=XCIBOl3FTKo

import random
import string


def generate_password(min_length, numbers=True, specials=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if specials:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if specials:
            meets_criteria = meets_criteria and has_special

    return pwd


min_length = int(input("Enter the minimum length: "))
input_has_num = input("has numbers? [Y/n]: ")
has_num = True
if input_has_num != "":
    has_num = input_has_num.lower() == "y"

input_has_spec = input("has specials? [Y/n]: ")
has_spec = True
if input_has_spec != "":
    has_spec = input_has_spec.lower() == "y"

print(generate_password(min_length, has_num, has_spec))


