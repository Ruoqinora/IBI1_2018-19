# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:06:19 2019

@author: 19305
"""
#input a string
s=input("Give me a string of words:")
#reverse the string
s=s[::-1]
#split the string into list
L=s.split()
reverseword=sorted(L)
reverseword.reverse()
print(reverseword)

