# Jack Caffrey
# Weekly Task 4 Program will allow the user enter a positive integer. If the number entered is even the program will divide it by 2. If the number is odd it will carry out a number of different calculations program will end when the current value is 1.

Entered_value = int(input("Please enter a positive number (integer): ")) #Allows user to enter a integer

if (Entered_value % 2) == 0:
      
      new_value = (Entered_value // 2)
      print (new_value)

elif  (Entered_value % 2) == 1:
         new_value = (Entered_value * 3 )
         
         print (new_value + 1)
  
elif Entered_value < 1:
         print ("Please Enter a positive integer")              