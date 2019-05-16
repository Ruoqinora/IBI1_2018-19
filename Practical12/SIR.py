# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:05:59 2019

@author: 19305
"""

#import neccesary libraries
import numpy as np
import matplotlib.pyplot as plt
#defined necessary parameters
S=9999
I=1
R=0
N=10000
beta=0.3
gamma=0.05
#creat three arrays
matrix1=[9999]
matrix2=[1]
matrix3=[0]


for i in range(1,1001):# run for 1000 times
    r1=np.random.choice(range(2),S,p=[1-beta*I/N,beta*I/N])
    s1=sum(r1)
#print(r1)
    S=S-s1
#print(S)
    I=I+s1
#print(I)
    matrix1.append(S)
    #matrix2.append(I)
    r2=np.random.choice(range(2),I,p=[1-gamma,gamma])
    s2=sum(r2)# sum all zeros and ones, to get the number of infected
    I=I-s2
    R=R+s2
    matrix2.append(I)
    matrix3.append(R)
#print(matrix1)
#print(matrix2)
#print(matrix3)
#make the plot
plt.plot(matrix1,label="susceptible")
plt.plot(matrix2,label="infected")
plt.plot(matrix3,label="recovered")
plt.title("SIR model")
plt.xlabel("Time")
plt.ylabel("Number of people")
plt.legend()# to show the labels
plt.show()
    
    
