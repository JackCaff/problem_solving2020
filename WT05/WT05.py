#Jack Caffrey 
# Allows the user know what day of the week it is
 
import datetime # Imports current time and date from library 

now = datetime.datetime.now()  
# print("now", now) display the exact time the progam is run 

day = now.day 
print("It is the ", day," day of the month") # if required can display the exact date the progam is run

weekday = now.weekday()

# displays the name of the day to the user 
if weekday == 0:
     print ("Today is Monday")
elif weekday == 1:
     print ("Today is Tuesday")
elif weekday == 2:
     print ("Today is Wednesday")
elif weekday == 3:
     print ("Today is Thursday")
elif weekday == 4:
     print ("Today is Friday")
elif weekday == 5:
     print ("Today is Saturday")
else: 
     print ("Today is Sunday")

## print ("Weekday is: ",weekday)

if weekday <=4: # if the value returned from weekday is less then on equal to 4 it is a weekday. 
     print (" Yes, unfortunately today is a weekday")
else: 
    print ("It is the weekend, yay!")
