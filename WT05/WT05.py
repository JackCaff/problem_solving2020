# Allows the user know what day of the week it is
# trial program to understand logic 
#Jack Caffrey 

import datetime

now = datetime.datetime.now()

print ("now", now)

day = now.day

print ("Day is", day)

weekday = now.weekday()


if weekday == [0,1,2,3,4]:

    print (" Yes, unfortunately today is a weekday")

else: 

    print ("It is the weekend, yay!")
