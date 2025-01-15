# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 13:32:55 2025

@author: KoKe
"""
import math

ia=input("Hva er diameteren på sirkelen? ")
ib=input("hva er høyden på trekanten? ")

a=float(ia)
b=float(ib)

"""
brare for å gjøre det litt lettere under utvikling.
a= 4.0
b= 6.0
"""
#Sirkel arial
radius=a/2
pi=math.pi
a_sirc= pi * (radius ** 2)/2

#Sirkel omkrets

o_sirc = (2 * pi * radius)/2

#Arial av 3kant

a_3k= (a*b)/2

#Omkrets 3kant

#legger inn vinkelen for en rettvinkelt trekant, også regner den om til radianer
v=90 
v_rad = math.radians(v)
#Regner ut lengden på dne ukjente siden som vi kaller c
c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(v_rad))

#rydder bare litt opp
o_trekant = c
#print ("omkrets på 3kant = ", c+a+b)



#svar
#Omkrets på halve cirkelen og trekanten minus a
print("Omkrets på halve cirkelen og trekanten, minus a for å få ytre omkrets =", o_sirc + o_trekant - a)
#Arial på halve cirkelen og hele trekanten
print("Arial på halve cirkelen og hele trekanten = ", (a_sirc/2)+a_3k)