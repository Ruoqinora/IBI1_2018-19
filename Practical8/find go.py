# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:00:39 2019

@author: 19305
"""
#import necessary libraries
import xml.dom.minidom
import re
import pandas as pd

#open files
filePath=r'D:\IBI\IBI1_2018-19\Practical8';#file path
fileName='go_obo.xml';
resName='autophagosome.xlsx'
file=filePath+'/'+fileName
res=filePath+'/'+resName




re_immu=re.compile(r'autophagosome')# replace autophagosome with re_immu for later search
#fuction to find childnodes
def Child(id,resultset):#count childnodes
    for t in go:
        parents=t.getElementsByTagName('is_a')#find childnodes
        geneid=t.getElementsByTagName('id')[0].childNodes[0].data
        for parent in parents:
            if parent.childNodes[0].data==id:
                resultset.add(geneid)
                #print(resultSet)
                Child(geneid,resultset)
#create a pandas.Dataframe to store the output
df=pd.DataFrame(columns=['id','name','defination','childnodes'])

#create the DOM tree
tree =xml.dom.minidom.parse(file)
obo=tree.documentElement
go=obo.getElementsByTagName('term')
for term in go:
    defstr=term.getElementsByTagName('defstr')[0].childNodes[0].data
    #find terms that contain the word 'autophagosome'
    if re_immu.search(defstr):
        id=term.getElementsByTagName('id')[0].childNodes[0].data
        name=term.getElementsByTagName('name')[0].childNodes[0].data
        resultset=set()
        Child(id,resultset)
        df=df.append(pd.DataFrame({'id':[id],'name':[name],'defination':[defstr],'childnodes':[len(resultset)]}))
        print(id,len(resultset))
        #only print these two elements but all in excel file.
#save to excel
df.to_excel(res,index=False)
                