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

outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1


S=9999
I=1
R=0
beta=0.3
gamma=0.05

# find infected points
infectedIndex = np.where(population==1)
#because tuple can not be changed, create arrays
infectedIndex2=infectedIndex[0]
infectedIndex3=infectedIndex[1]

#print(type(infectedIndex2))

# loop through all infected points
for j in range(100):
    for i in range(len(infectedIndex2)):
        # get x, y coordinates for each point
        x = infectedIndex2[i]
        y = infectedIndex3[i]
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
                            if population[xNeighbour,yNeighbour]==1:
                                infectedIndex2=np.append(infectedIndex2,xNeighbour)
                                infectedIndex3=np.append(infectedIndex3,yNeighbour)

                        if population[xNeighbour,yNeighbour]==1:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(3),1,p=[0,1-gamma,gamma])
    
    
    
    plt.figure(figsize=(6,4),dpi=150)
    plt.imshow(population,cmap='viridis',interpolation='nearest')
plt.show()