# Jack Caffrey 
# A function to find the square root of numbers (Newtons method of finding square roots)
# ref https://pages.mtu.edu/~shene/COURSES/cs201/NOTES/chap04/sqrt.html formula used to establsh newtons method

b = float(input("Please enter a positive integer: ")) # User Input Value 

def sqrt(x): # declaring square root function 

    b = x #takes the value entered by the user and converts into the 'x' value required for the formula. 
    b1 = b * (10**-10) #(10**-10) = 0.0001 
        
    while abs(x - b * b) > b1: #abs retruns the absoulte value of the calculation (x - b * b ) 
                               #loop continues until value is less then b1 value
       b = ((b + x/b) / 2) 
    
    return b   

print (round(sqrt(b),2)) # prints the result rounding to two decimal places.







