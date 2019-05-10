# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:06:19 2019

@author: 19305
"""

s=input("Give me a string of words:")
s=s[::-1]
L=s.split()
L1=sorted(L)
L1.reverse()
print(L1)


s=input()
words=s.split(" ")
reversewords=[]
for word in words:
    reversewords.append(word[::-1])
reversewords.sort(reverse=True)
print(reversewords)