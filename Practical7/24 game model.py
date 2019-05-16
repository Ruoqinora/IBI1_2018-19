# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:25:50 2019

@author: 19305
"""
#import neccessary libraries
import re
from fractions import Fraction
# determine whether the input numbers are integers between 1 and 23
re_numtest=re.compile(r'(^[1-9]$)|(^1[0-9]$)|(^2[0-9]$)')
i=1
while i:
    i=0
    data=input('please input numbers to computer 24:(use\',\' to dividethem)\n')
    numlist=data.split(',')
    for char in numlist:
        if re_numtest.match(char):
            continue
        else:#the input number should be an integer between 1 and 23
            print('The input number must be intergers from 1 to 23')
            i=1
            break
num=list(map(int,numlist))#put numbers in a list

#recursion times
count=0

#way to get 24
solution=0

#define a function for recursion
#n is len(num)

def func(n):
    global count
    global solution
    count=count+1
    
    if n==1:
        if(float(num[0])==24):
            solution=solution+1
            return 1
        else:
            return 0
    #select two different numbers and test all operations
    for i in range(0,n):
        for j in range(i+1,n):
            a=num[i]
            b=num[j]
            num[j]=num[n-1]# select the last number as b
            
            #replace a with the operation results of a and b
            num[i]=a+b 
            if(func(n-1)):
                return 1
            
            num[i]=b-a
            if(func(n-1)):
                return 1
            
            num[i]=a*b
            if(func(n-1)):
                return 1
            
            # to determine whether a/b or b/a makes sense.
            if a:
                #floats are not precise
                num[i]=Fraction(b,a)
                if(func(n-1)):
                    return 1
                
            if b:
                num[i]=Fraction(a,b)
                if(func(n-1)):
                    return 1
            
            #Backtracking
            num[i]=a
            num[i]=b
    return 0

if (func(len(num))):# if there exist sulotions
    print('YES')
else:
    print('NO')
print('Recursion times:',count,',Solution:',solution) #return recursion times and numbers of solutions           
        
        
