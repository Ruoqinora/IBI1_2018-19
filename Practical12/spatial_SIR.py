# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:11:03 2019

@author: 19305
"""

#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#make array of all susceptible population
population=np.zeros((100,100))
#print(population[4,12])

outbreak=np.random.choice(range(100),2)# random selection of one infected individual
population[outbreak[0],outbreak[1]]=1

#define necessary parameters
S=9999
I=1
R=0
beta=0.3
gamma=0.05

# find infected points
infectedIndex = np.where(population==1)

# loop through all infected points
for j in range(0,101):
    infectedIndex = np.where(population==1)
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        #recover
        population[x,y]=np.random.choice(range(1,3),1,p=[1-gamma,gamma])[0]
        # infect each neighbour with probability beta
        # infect all 8 neighbours (this is a bit finicky, is there a better way?):
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                # don't infect yourself! (Is this strictly necessary?)
                if (xNeighbour,yNeighbour) != (x,y):
                    # make sure I don't fall off an edge
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        # only infect neighbours that are not already infected!
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
                            
#make plots  
    if j in [0,10,50,100]:#print several plots from all
        plt.figure(figsize=(6,4),dpi=150)
        plt.imshow(population,cmap='viridis',interpolation='nearest')
