#LEVEL 2: TASK 3: Password Strength Checker.

import re

password = input("enter your password: ") 
if len(password) < 8:
    print("password must be at least 8 characters long.")
elif not re.search("[A-Z]", password):
    print("password must contain at least one uppercase letters.")
elif not re.search("[a-z]", password):
    print("password must contain at least one lowercase letters.") 
elif not re.search("[0-9]", password):
    print("password must contain at least one number.")
else:
    print("password is strong")