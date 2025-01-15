# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 14:18:38 2025

@author: ul54
"""

#import math
#import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

# Define the function f(x)
def f(x):
    return -x**2 - 5

# Generate x values from -10 to 10
x = np.linspace(-10, 10, 200)

# Calculate y values using the function
y = f(x)

# Create the plot
plt.plot(x, y, label='f(x) = -x^2 - 5')

# Add title and labels
plt.title('Plot of f(x) = -x^2 - 5')
plt.xlabel('x')
plt.ylabel('f(x)')

# Add a legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()