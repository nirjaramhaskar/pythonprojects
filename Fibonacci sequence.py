#LEVEL 2: TASK 4: FIBONACCI SEQUENCE

n=int(input("Enter the terms till you want"))
n1, n2 = 0, 1
count = 0
if n<= 0:
   print("Enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print (n1)
else:
   print("Fibonacci sequence:")
   while count <n:
      print (n1)
      S = n1 + n2
      n1 = n2
      n2 = S
      count += 1