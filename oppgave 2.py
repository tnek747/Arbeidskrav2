# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:05:05 2024

@author: KoKe
"""
# import packages
import math

#code
#x = antall elever som skal ha pizza 
x=int(input("hvor mange er det i din klasse "))
#p = hvor mye av en pizza en elev spiser
p=0.25
print(x*p)
#Pizza er antall pizaer som må bestilles
pizza=math.ceil(x*p)
print("bestill", pizza, "store pizzaer fra Jeppes i Kongsberg")