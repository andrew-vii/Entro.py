#!/usr/bin/python

import requests
import os, os.path
import random
import time
from datetime import datetime
import re
import numpy as np
import matplotlib.pyplot as plt


print ("\n\nWelcome to Entro.py -- The Facebook OSINT Collection Tool")
print ("Version 0.4")
print ("\nUse CTRL-C to abort")
print ("---------------------------------------------------------\n\n\n")


#Accept arg for specified UID
uid = raw_input("Enter Facebook UID: ")


#Unix timestamp to DTG conversion
#dt = (datetime.fromtimestamp(unix_ts)).strftime('%Y-%m-%d %H:%M:%S') #unix_ts is the LAT data 


xvals=[]
yvals=[]

#Pull LATs from uid.txt as x-value, assign 1 to y value if LAT = 1, assign 0 otherwise

#WIP   - Need to have it check for the LAT =1. If it equals 1, set y value to 1 and x value to timestamp of pullcap file
							#If it equals more than 1, set y value to 0 and x value to timestamp of pullcap file   
							#We can add a second data point if LAT > 1, set y value to 1 and x value to LAT timestamp


a = open('/dir/path/Entropy/uidfiles/%s.txt'%uid,'r') #Uidfiles dirpath here
for i in a:
	match = re.findall(('\d+'), i)
	
	
	if int(match[0]) > 1:
		xvals.append(int(match[0]))
		yvals.append(1)
		xvals.append(int(match[1]))
		yvals.append(0)
	else:
		xvals.append(int(match[1]))
		yvals.append(1)
	
	#We just want to check if there are any digits in for vc and p, values don't matter right now
	if len(match) >= 4:
		xvals.append(int(match[1]))
		yvals.append(2)
		

conxvals=[]
#Unix timestamp to DTG conversion
for z in xvals:
		
	dt = (datetime.fromtimestamp(z)).strftime('%Y-%m-%d %H:%M:%S') #unix_ts is the LAT data 
	conxvals.append(dt)

fig, ax = plt.subplots()
ax.plot_date(conxvals, yvals, 'ro') #Looks like this takes two lists as input
#fig.gcf().autofmt_xdate()
fig.autofmt_xdate()
#plt.axis([2018-8-13_23:52:16,2018-8-17 16:32:29,-.1,1.1])
plt.show()
