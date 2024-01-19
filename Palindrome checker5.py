#Level 1:Task 5 Palindrome Checker


def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

my_string = input("Enter a string: ") 
if is_palindrome (my_string):
    print("The input string is a palindrome.")
else:
    print("The input string is not a palindrome.")