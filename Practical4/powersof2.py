# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:05:26 2019

@author: 19305
"""

#x1=2019
#find the number a1 which make sure 2**a1<2019

#then make x2=2019-2**a1
#find a2 which make sure 2**a2<x2
#blablabla
#finally when xn=x(n-1)-2**a(n-1)=0 done
#then 2019=2**a1+2**a2+……+2**a(n-1)

#define x as the power, count down from 13
x=13
#n as the input number
n=int(input())
#a as the output
a=str(n)+" is 2**"
# while loop
while n!=0:
    if n-2**x<0:
        x=x-1# continue another power number
        continue
    if n-2**x>0:
        a=a+str(x)+"+2**"
        n=n-2**x
        continue
    if n-2**x==0:
        a=a+str(x)
        break
print(a)
    
    
    



    
   

