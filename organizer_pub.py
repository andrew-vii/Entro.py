#!/usr/bin/python

import requests
import os, os.path
import sys
import random
import time
from datetime import datetime
import re

print "\n\nWelcome to Entro.py -- The Facebook OSINT Collection Tool"
print "Version 0.4"
print "\nUse CTRL-C to abort"
print "---------------------------------------------------------\n\n\n"

#Get count of files in pullcap directory, used for program completion status
filecount = len([name for name in os.listdir("pullcapfiles/")]) #Put directory location of pullcap directory here
loopcount=0

#Get list of all pullcap files retrieved by the main puller program
pullcaps = os.listdir("pullcapfiles/") #Directory location of pullcap files here

#Write list of pullcap files to text file
d = open("pullcaplist.txt",'w') #Location of pullcap list file here
d.writelines(["%s\n" %item for item in pullcaps])
d.close()

#Get UIDs and LATs from all pullcap files
c = open('uidlist.txt','w+') #Location of UIDlist file here
with open('pullcaplist.txt','r') as b: #Location of pullcaplist file here
	for k in b:
		loopcount+=1
		percent = 100 * loopcount / filecount
		sys.stdout.write("\rOrganizing files....%d%% complete." %percent)
		k=k.rstrip()
		a = open('pullcapfiles/%s' %k,'r') #Pullcap file directory here
		astr = a.read()
		auid = re.findall('"\d+":{"lat":\d+', astr) #Produces list of UIDs and LATs from a pullcap file
		nuid = re.findall('"\d+":{"lat":-1', astr) #Produces list of UIDs and LATs from pullcap file with LAT of -1, we have to do this seperately because Python 2.7 is grumpy if we put ()'s in regex
		unkuid = re.findall('\d+":{"lat":\d+,"p":\d+,"vc":\d+}', astr) #Produces list of UIDs and LATs that have the 'p' or 'vc' parameters set
		for x in auid:
			matcher = re.findall(('\d+'), x)
			seluid = matcher[0]
			sellat = matcher[1]
			#seluid = re.match('"\d+"', x).group(0).strip('\"') #Strips out UID from file
			#sellat = re.match('d+', x).group(0)     #.replace(':','') #Strips out lat from pullcap file
			c.writelines("%s\n" %seluid) 							#Adds UID to uidlist.txt
			b = open('uidfiles/%s.txt' %seluid,"a") #Creates uid.txt file for each unique UID,uidfiles dirpath here
			b.writelines("%s:%s\n" % (sellat, k) ) #Writes LAT and pullcap timestamp to corresponding UID file
			b.close()
			
		for z in nuid:
			negmatcher = re.findall(('\d+'), z)
			neguid = negmatcher[0]
			neglat = negmatcher[1]
			c.writelines("%s\n" %neguid) 							#Adds UID to uidlist.txt
			e = open('uidfiles/%s.txt' %neguid,"a") #Creates uid.txt file for each unique UID,uidfiles dirpath here
			e.writelines("%s:%s\n" % (neglat, k) ) #Writes LAT and pullcap timestamp to corresponding UID file
			e.close()
		
		for y in unkuid:
			unkmatcher = re.findall(('\d+'), y)
			foruid = unkmatcher[0]
			forlat = unkmatcher[1]
			pval = unkmatcher[2]
			vcval = unkmatcher[3]
			g = open('uidfiles/%s.txt' %foruid,"a") #Creates uid.txt file for each unique UID, uidfiles dirpath here
			g.writelines("%s:%s::%s:%s\n" % (forlat,k,pval,vcval) ) #Writes LAT and pullcap timestamp to corresponding UID file
			g.close()
									 			
print("\n\n")
	
