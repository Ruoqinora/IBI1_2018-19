# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:16:39 2019

@author: 19305
"""

import os


def xml_to_cps():
    import os
    import xml.dom.minidom
    
    # first, convert xml to cps   
    os.system("CopasiSE.exe -i predator-prey.xml -s predator-prey.cps")  
    cpsTree = xml.dom.minidom.parse("predator-prey.cps")
    cpsCollection = cpsTree.documentElement
    
    reportFile = xml.dom.minidom.parse("report_ref.xml")
    reportLine = reportFile.documentElement
    
    tasks = cpsCollection.getElementsByTagName("Task")
    for task in tasks:
        if task.getAttribute("name")=="Time-Course":
            task.setAttribute("scheduled","true")
            task.insertBefore(reportLine,task.childNodes[0])
            break
        
    
    for taskDetails in task.childNodes:
        if taskDetails.nodeType ==1:
            if taskDetails.nodeName == "Problem":
                problem = taskDetails
                
    for param in problem.childNodes:
        if param.nodeType ==1:
            if param.getAttribute("name")=="StepNumber":
                param.setAttribute("value","200")
            if param.getAttribute("name")=="StepSize":
                param.setAttribute("value","1")
            if param.getAttribute("name")=="Duration":
                param.setAttribute("value","200")
           
            
    report18 = xml.dom.minidom.parse("report18.xml")
    report = report18.documentElement
    
    listOfReports  =  cpsCollection.getElementsByTagName("ListOfReports")[0]
    listOfReports.appendChild(report)
    
    cpsFile = open("predator-prey.cps","w",encoding='utf-8')#encoding='utf-8' to solve problems
    cpsTree.writexml(cpsFile)
    cpsFile.close()
    
xml_to_cps()#run the function
os.system('CopasiSE.exe predator-prey.cps')
os.chdir("C:/Users/19305/Desktop/IBI/week13 copasi")
#read data from csv file
import re
import numpy
file=open('modelResults.csv','r')
reader=file.readlines()
count=0
names=[]
data=[]
for line in reader:
    if count==0:
        names=re.split(r',+',line)
        count=1
    else:
        r=re.split(r',+',line)
        del(r[0])# remove 'A','B' in the first line 
        data.append(r)
results=numpy.array(data)
results=results.astype(numpy.float)
#print(results)

#make plot populations against time
import matplotlib.pyplot as plt
plt.figure(figsize=(6,4),dpi=150)
plt.plot(results[:,0],label='Predator (b=0.02,d=0.4)')
plt.plot(results[:,1],label='Prey (b=0.1,d=0.02)')
plt.xlabel('time')
plt.ylabel('population size')
plt.title('Time Course')
plt.legend(loc='upper right')#make the location of label on the upper right 
#plots predator population against prey population.
plt.figure(figsize=(6,4),dpi=150)
plt.xlabel("predator(b=0.02.d=0.4)")
plt.ylabel("prey(b=0.1,d=0.02)")
plt.title('Limit cycle')
plt.plot(results[:,0],results[:,1])
        
#open xml file       
#changing values and running the simulation again
#define four new parameters
#import xml.dom.minidom change parameters and save them
#make the plot


#simulate many simulations
#select combination of parameters
#make seperate plots by creating loops
#print the max number of predator and prey















