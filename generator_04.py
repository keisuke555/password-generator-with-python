# Simple Password Generator in Python
# https://www.youtube.com/watch?v=rHTwjV1ORUQ&t=229s

import random

upper_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letter = "abcdefghijklmnopqrstuvwxyz"
digits_letter = "0123456789"
symbols_letter = "!@#$%^&*()_+|~-=`[]{},./<>?;':\\"

upper, lower, digits, symbols = True, True, True, True

allChars = ""

if upper:
    allChars += upper_letter

if lower:
    allChars += lower_letter

if digits:
    allChars += digits_letter

if symbols:
    allChars += symbols_letter

length = 10
count = 10

# seedを設定することでrandom関数の実行結果として同じレスポンスが得られる
# seed = "myseed"
# random.seed(seed)

for x in range(count):
    password = "".join(random.sample(allChars, length))
    print("パスワード:" + password)

