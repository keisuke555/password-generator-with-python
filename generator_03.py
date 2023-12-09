# Python Beginner Project: Password Generator
# https://www.youtube.com/watch?v=VEfEzl9mgt0
import secrets
import string
import random

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
special = string.punctuation
allChars = lower + upper + digits + special
password = ""

pwLen = int(input("How long should the password be? "))  # パスワードの長さどうする？
minUpper = int(input("Minimum Upper Case "))  # 大文字は最低何文字？
minLower = int(input("Minimum Lower Case "))  # 小文字は最低何文字？
minDigits = int(input("Minimum Numbers "))  # 数字は最低何文字？
minSpec = int(input("Minimum Special "))  # 特殊文字は最低何文字？

# まずは最低文字数の要件を満たす
for i in range(minUpper):
    password += "".join(random.choice(secrets.choice(upper)))

for i in range(minLower):
    password += "".join(random.choice(secrets.choice(lower)))

for i in range(minDigits):
    password += "".join(random.choice(secrets.choice(digits)))

for i in range(minSpec):
    password += "".join(random.choice(secrets.choice(special)))

# 文字数不足分をallCharsから補足
remaining = pwLen - minUpper - minLower - minDigits - minSpec

for i in range(remaining):
    password += "".join(random.choice(secrets.choice(allChars)))

# 最後にシャッフルして出力
password = list(password)
random.shuffle(password)
print("".join(password))
