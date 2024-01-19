#LEVEL 1 : TASK 4: CALCULATOR PROGRAM


num1 = float(input("enter first number here: "))
num2=float(input("enter second number here: "))

print("press 1 for addition \npress 2 for subtract \npress 3 for multiply \npress 4 for division \npress 5 for modulus")

choice = int(input("enter your choice from 1-5: "))

if choice == 1:
        print("The addition of given two numbers is", num1 + num2)
elif choice == 2:
        print("The subtraction of given two numbers is", num1 - num2) 
elif choice == 3:
        print("The multiplication of given two numbers is", num1* num2) 
elif choice == 4:
        print("The division of given two numbers is", num1 / num2) 
elif choice == 5:
        print("The modulus of given two numbers is", num1 % num2)
else:
        print("Invalid Input")