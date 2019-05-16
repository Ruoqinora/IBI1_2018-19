# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:06:23 2019

@author: 19305
"""
p=0
#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
for i in range(1,12):# change the percentage
    # define necessary parameters
    N=10000
    V=int(p*N)
    S=9999-V
    I=1
    R=0
    l=str(int(p*100))+"%"# late used for label
    p=p+0.1

    beta=0.3
    gamma=0.05
#creat necessary arrays
    matrix1=[S]
    matrix2=[1]
    matrix3=[0]
    for i in range(1,1001):# run 1000 times
        r1=np.random.choice(range(2),S,p=[1-beta*I/N,beta*I/N])
        s1=sum(r1)#sum zeros and ones to determine teh number of infected ones
#print(r1)
        S=S-s1
#print(S)
        I=I+s1
#print(I)
        matrix1.append(S)
        r2=np.random.choice(range(2),I,p=[1-gamma,gamma])
        s2=sum(r2)
        I=I-s2
        R=R+s2
        matrix2.append(I)#expand arrays
        matrix3.append(R)
        #print(matrix1)
    plt.plot(matrix2,label=l)
#plt.plot(matrix3,label="recovered")
    plt.title("SIR model")
    plt.xlabel("Time")
    plt.ylabel("Number of people")
    plt.legend()#show labels
plt.show()
    