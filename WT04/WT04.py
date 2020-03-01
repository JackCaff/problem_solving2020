# Jack Caffrey
# Ref A Whirlwind tour of python "Jake VanderPlas" https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf 
# Ref Class discussion board
# Weekly Task 4 Program will allow the user enter a positive integer. 
# If the number entered is even the program will divide it by 2. 
# If the number is odd it will carry out a number of different calculations program will end when the current value is 1.

Num = int(input("Please enter a positive integer: ")) # Allows a user to enter a positive integer

print (Num,end=" ") # Prints the integer entered first
while Num !=1: # while loop continues until the value equals 1. When it equals 1 the program will end.
   
   # determines if integer entered is odd or even
   if Num % 2 ==0: 
      Num = Num // 2
      print(Num, end=" ")

   else: 
      Num = (Num * 3) + 1
      print(Num, end=" ")