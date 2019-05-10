# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:38:26 2019

@author: 19305
"""
#define a positive integer
#first test whether n can be divided by 2 or not
#if n can not be divide by two, multiply it by 3 and add 1
#use while loop to stop the code when the result is 1
c1=3
while c1!=1:
    if c1%2==0:
        c1=c1/2
    else:
        c1=3*c1+1
    print(c1)