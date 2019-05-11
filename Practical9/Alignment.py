# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:02:55 2019

@author: 19305
"""

human='MLSRAVCGTSRQLAPVLGYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK'
mouse='MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK'

#create a two dimension dictionary
def readdic(filename):
    handle=open(filename,"r")
    content=handle.readlines()
    handle.close()
    
    dic={}
    letters=[]
    
    first=True
    for line in content:
        splitted=line.split()
        if first:
            for a in splitted:
                dic[a]={}
                letters.append(a)
            first=False
        else:
            a=splitted[0]
            for i in range(1,len(splitted)):
                b=letters[i-1]
                dic[a][b]=splitted[i]
    return dic
dic=readdic('blosum62.txt')
#print(dic)

   
#calculate the score
score=0
for i in range(0,len(human)):# same length
    score=score+(int(dic[human[i]][mouse[i]]))
    #print(score)
print('The BLOSUM score is:'+str(score))
    