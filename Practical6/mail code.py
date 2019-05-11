# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 15:33:03 2019

@author: 19305
"""
#import necessary libraries
import smtplib
from smtplib import SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import getpass
import re

# read information from the excel file
address=open('address_information.csv')
# select different elements
correct_address=[]
name=[]
subject=[]
for line in address:
    line=re.split(',',line)
    if re.match(r'(\S+)@(\S+)+(\.\S)',line[1]):#select correct address
        print(line[1],':','Correct address')
        correct_address.append(line[1])#add correct addresses to a list
        name.append(line[0])
        subject.append(line[2])
    else:
        print(line[1],':','Wrong address')
address.close()
#read content from body.txt
with open(r"body.txt",'r') as content:
    data=content.read()
    data1=data[::]
    
username=input('Please input your zju username:')
password=getpass.getpass('please input the password:')
#make password be invisible
yourname=input('Please input your name:')

for i in range(3):
    data=data1.replace('User',name[i])# change 'User' in content into names
    # send emails
    try:
        sender=username+'@zju.edu.cn'
        receivers=correct_address[i]
        mailserver=smtplib.SMTP('smtp.zju.edu.cn',25)
        mailserver.login(username,password)
        
        msg=MIMEMultipart()
        msg['To']=Header(name[i],'utf-8')
        msg['Subject']=Header(subject[i],'utf-8')
        msg['From']=Header(yourname,'utf-8')
        msg.attach(MIMEText(data,'plain'))
        
        text=msg.as_string()
        mailserver.sendmail(sender,receivers,text)
        mailserver.quit()
        print('Mail sent successfully!')
    except SMTPException:
        print("Error:unable to send emails")