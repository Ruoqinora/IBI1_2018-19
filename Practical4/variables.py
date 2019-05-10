# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:31:14 2019

@author: 19305
"""

a = 155
b = 155155
c = b/7
d = c/11
e = d/13
print (e)

b = 155155
p = b%7
print (p)

X=True
Y=False
Z=(X and not Y) or (Y and not X)
if Z:
    print("Z is true")
else:
    print("Z is not true")
    
X=False
Y=True
W=(X!=Y)
if W:
    print("W is true")
else:
    print("W is not true")