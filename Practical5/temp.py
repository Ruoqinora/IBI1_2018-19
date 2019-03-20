 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


sequence =input()
sequence = sequence.split(' ')
mydict={}
for word in sequence:
    if word in mydict:
        mydict[word]+=1
    else:
        mydict[word]=1
print(mydict)

import matplotlib.pyplot as plt

labels='A','T','C','G'
sizes=tuple(mydict.values())
explode=(0,0.1,0,0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal') 

plt.axis('equal')
plt.show()











