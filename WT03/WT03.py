# Weekly Task 3 (Programming & Scripting)  Jack Caffrey
# Program allows a user enter a sentance and output every second letter of the sentence in reverse

sentence = input(str("Please enter your sentence: ")) #Allows user to enter a sentence

print ("Your sentence is:", sentence,) #Displays the sentence entered

sentence = sentence [::-1] #Reverses the sentence entered

print ("Your sentence in reverse is :",sentence,) # Prints the full sentence in reverse 

print ("Every second letter of the Sentence in reverse is: ", sentence [::2],) #Displays every second letter of the reversed sentence
