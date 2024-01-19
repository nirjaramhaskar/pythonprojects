#LEVEL 1: TASK 3: EMAIL VALIDATOR.
import re
regex= r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b'
user_email=input("Enter your Email:")

if(re.fullmatch (regex, user_email)): 
    print("Valid Email")
else:
    print("Invalid Email")