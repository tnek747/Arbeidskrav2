# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 20:01:17 2024

@author: KoKe
"""
import datetime

a = int(input('Hvilket år er du født? ') )
x = datetime.datetime.now()
t=int((x.strftime("%Y")))
print("I løpet av",t,"blir du", t-a, "år:-)")