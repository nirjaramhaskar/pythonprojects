#LEVEL 1: TASK 2: TEMPERATURE CONVERSION
print("choose 1 or 2 \n")
print("1.Convert temperature from Celsius to Fahrenheit \n")
print("2.Convert temperature from Fahrenheit to Celsius \n") 
option =int(input("Choose any Option(1 or 2) : "))
if option == 1:
   print("Convert temperature value from Celsius to Fahrenheit \n")
   c = float(input("Enter Temperature in Celsius: "))
   F = (c*9/5)+32
   print("Temperature in Fahrenheit -",F, "Fahrenheit")
elif option == 2:
    print("Convert temperature value from Fahrenheit to Celsius \n")
    F = float(input("Enter Temperature in Fahrenheit: "))
    c=(F-32)*5/9
    print("Temperature in Celsius -",c,"celsius")
else:
    print("Invalid Option")