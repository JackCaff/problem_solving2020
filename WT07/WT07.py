# Jack Caffrey

f = open('moby10b.txt', 'r')  #defines the file to read in the arguments
contents = f.read() #reads the content of the file 
count = 0  #Initialize the counter
for i in contents:
    if i == 'e':
        count = count + 1 #counter increments 1 every time the file reads lower case e

print (count) # prints the values of e's contained in the txt file

f.close() #closes read file


 