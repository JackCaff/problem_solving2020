# Weekly Task 2 (Programming & Scripting)  Jack Caffrey
# Code allows the user to input their weight (KG) & height (CM) and out puts their  BMI

weight = float(input("Please enter your Weight in Kilograms (KG): "))
height = float(input("Please enter your Height in centimetres (CM): "))

# print ("The weight entered is weight" , weight , "and height entered is" , height,) code line used to verify inputs working correctly

Meters_Squard = ((height * height) / 100) #converts CM to Meters Squared

BMI = ((weight / Meters_Squard) * 100) # Calculates BMI 

new_BMI = round(BMI, 2) # Rounds BMI to 2 decimal places
print ("Your BMI is" , new_BMI) #displays users BMI 