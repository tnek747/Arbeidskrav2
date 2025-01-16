# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 14:18:38 2025
PS, Måtte bruke copilot i utstrakt grad for denne oppgaven.
@author: KoKe
"""

#import math
#import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

# definerer funksjonen x
def f(x):
    return -x**2 - 5

# lager alle datapunkter fra -10 til 10.
x = np.linspace(-10, 10, 200)

# lager y basert på funksjoner x
y = f(x)

# bruker plot for å lage graf
plt.plot(x, y, label='f(x) = -x^2 - 5')

# pynter grafen og dataene
plt.title('Plot of f(x) = -x^2 - 5')
plt.xlabel('x')
plt.ylabel('f(x)')

# legger inn fuksjonen som i grafen
plt.legend()

# tegner grafen
plt.grid(True)
plt.show()