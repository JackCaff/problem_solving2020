# Jack Caffrey 
# Weekly Task 08
# Program that plot the functions of f(x), g(x)=x^2, h(x) = x^3 in the range 0 to 4.

import matplotlib.pyplot as plt # matplotlib.pyplot imported library 
import numpy as np

x = np.arange(0.0, 4.0, 1.0 )  # setting range 0 to 4 with 1.0 spacing between)

f = x       # defining f function
g = x**2    # defining g function
h = x**3    # defining h function

y1 = f      # defining y1 plot
y2 = g      # defining y2 plot
y3 = h      # defining y3 plot


plt.plot(x, y1, 'r', label ="f(x) = x")   #plots x vs y1
plt.plot(x, y2, 'b', label ="g(x) = x^2")  #plots x vs y2
plt.plot(x, y3, 'g', label ="h(x) = x^3")   #plots x vs y3

plt.legend() #displays labels
plt.title("Plots of the function as shown in the legend for range 0 to 4") #displays graph title
plt.xlabel (" x-axis") #displays x-axis heading
plt.ylabel (" y-axis") #displays y-axis heading
plt.show() #displays graph 

