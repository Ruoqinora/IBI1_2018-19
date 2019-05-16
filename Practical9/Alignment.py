# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:02:55 2019

@author: 19305
"""

human='MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK'
mouse='MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK'
random='WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL'
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
score1=0
for i in range(0,len(human)):# same length
    score1=score1+(int(dic[human[i]][mouse[i]]))# read the corresponding numbers
    #print(score)
print('The BLOSUM score for human mouse comparison is:'+str(score1))

score2=0
for i in range(0,len(human)):# same length
    score2=score2+(int(dic[human[i]][random[i]]))# read the corresponding numbers
    #print(score)
print('The BLOSUM score for human random seq comparison is:'+str(score2))

score3=0
for i in range(0,len(human)):# same length
    score3=score3+(int(dic[random[i]][mouse[i]]))# read the corresponding numbers
    #print(score)
print('The BLOSUM score for mouse random seq comparison is:'+str(score3))
 #calculate identities   
count1=0
for i in range(0,len(human)):
    if human[i]==mouse[i]:
        count1=count1+1
#print(count)
identity=count1/len(human)
identity=str(identity*100)+'%'
print('Identity for human mouse comparison is :'+identity)

count2=0
for i in range(0,len(human)):
    if human[i]==random[i]:
        count2=count2+1
#print(count)
identity2=count2/len(human)
identity2=str(identity2*100)+'%'
print('Identity for human random seq comparison is:'+identity2)

count3=0
for i in range(0,len(human)):
    if mouse[i]==random[i]:
        count3=count3+1
#print(count)
identity3=count3/len(human)
identity3=str(identity3*100)+'%'
print('Identity for human random seq comparison is:'+identity3)