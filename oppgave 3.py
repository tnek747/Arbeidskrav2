# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 20:19:42 2024

@author: KoKe
"""

import numpy as np
v_grad = float(input('Skriv inn gradtallet: ' ))
v_rad = v_grad*np.pi/180

v_rad=round(v_rad, 4)
print('radianene blir ', v_rad)