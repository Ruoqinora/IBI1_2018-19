 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#input a DNA sequence
sequence =input("Please enter a DNA sequence:")
sequence=list(sequence)# split the sequence into a list
#creat a dictionary to count numbers
mydict={}
for word in sequence:
    if word in mydict:
        mydict[word]+=1
    else:
        mydict[word]=1
print(mydict)
#make plots
import matplotlib.pyplot as plt

labels='A','T','C','G'
sizes=tuple(mydict.values())
explode=(0,0,0,0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',#calculate the percentage
        shadow=False, startangle=90,)
ax1.axis('equal') 
plt.title("frequency of nucleotides")











