# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 14:45:37 2016

@author: student
"""

import smtplib

to = '8482194611@tmomail.net'
gmail_user = "goannabananasavana@gmail.com"
gmail_pwd = "U7CWbg4wJkrmXB"
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)

header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n ' + 'Subject: ANNOYING' + '\n'
print(header)
msg = header + '\n happy 7th of july \n\n'
smtpserver.sendmail(gmail_user, to, msg)
print('done!')
smtpserver.close()