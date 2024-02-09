#!/usr/bin/env python
# coding: utf-8

integers = []

for n in range(1, 20000): 
    if 1997 % (n**2 + (n+1)**2) == 0:
        integers.append(n)
        
print(len(integers))

integers2 = []

for n in range(1, 20000): 
    if 2009 % (n**2 + (n+1)**2) == 0:
        integers2.append(n)
        
print(len(integers2))

integers3 = []

for n in range(1, 20000): 
    if 2022 % (n**2 + (n+1)**2) == 0:
        integers3.append(n)
        
print(len(integers3))

