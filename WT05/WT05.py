#Jack Caffrey 
# Allows the user know what day of the week it is
 
import datetime # Imports current time and date from library 

now = datetime.datetime.now()  
# print("now", now) display the exact time the progam is run 

day = now.day 
# print("Date is", day) if required can display the exact date the progam is run

weekday = now.weekday()

if weekday == (0,1,2,3,4):
     print (" Yes, unfortunately today is a weekday")
else: 
    print ("It is the weekend, yay!")
