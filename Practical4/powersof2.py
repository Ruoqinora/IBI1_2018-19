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

x=2019
a=1
while x>0:
    while 2**a<x:
          a=a+1
    a=a-1
    x=x-2**a
    print(a)
    



    
   

