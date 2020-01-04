#!/usr/bin/python

#Main entro.py program, makes requests to Facebook for friendlist chat activity data

import requests
import os 
import time
from datetime import datetime
import re

print "\n\nWelcome to Entro.py -- The Facebook OSINT Collection Tool"
print "Version 0.4"
print "\nUse CTRL-C to abort"
print "---------------------------------------------------------\n\n\n"

pullcount = 0
newseq = 0
seqcount = 1

while 1:
	headers = {
    	'origin': 'https://www.facebook.com',
    	'accept-encoding': 'gzip, deflate, br',
    	'accept-language': 'en-US,en;q=0.9',
    	'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    	'accept': '*/*',
    	'referer': 'https://www.facebook.com/',
    	'authority': '4-edge-chat.facebook.com',
		'cookie': '', #Copy your Facebook cookie here, can get this from the network request pane in your web browser
	}

	params = (
  		 ('channel', '666666'), #Insert channel here, format should be a_###########
    	('seq', '1'),
    	('partition', '-2'),
    	('clientid', '6666'), #Insert your clientID here, format should be ##a##a#
    	('cb', '9oum'),
    	('idle', '0'),
    	('qp', 'y'),
    	('cap', '8'),
    	('pws', 'fresh'),
    	('isq', '66576'),
    	('msgs_recv', '0'),
    	('uid', '666666666') #Insert your Facebook UID here
    	('viewer_uid', '66666666666'), #Insert your Facebook UID here
    	('sticky_token', '1003'),
    	('sticky_pool', 'ash4c09_chat-proxy'),
    	('state', 'active'),
	)

	response = requests.get('https://4-edge-chat.facebook.com/pull', headers=headers, params=params)

	
	#Make initial pull request
	print("Sending pull request...")
	print("%d pull requests sent this session.\n\n" %pullcount)
	reqpull = requests.get('https://4-edge-chat.facebook.com/pull', headers=headers, params=params)

	#Error checking for correct seq number
	if "fullReload" or "deltaflow" in reqpull.text:
		print("Incorrect sequence number")
		#newseq = re.findall(r'\d+', reqpull.text)
		#print("%s is new seq num" %newseq[0])
		#Re-send request with corrected seq number set back to 0
		parlst = list(params)
		parlst[1] = ('seq',0)
		params = tuple(parlst)
		#Sending new pull request
		print("Sending new pull request...")
		reqpull = requests.get('https://4-edge-chat.facebook.com/pull', headers=headers, params=params)
		
	#Send pull request output to file
	t = time.localtime()
	#timestamp = time.strftime('%b-%d-%Y_%H%M', t)
	timestamp = int(time.time())
	filename = 'pullcapfiles/PULLCAP_%s.txt' %timestamp #Place the directory location of the PULLCAP dir here
	f = open(filename,'w')
	enc = reqpull.text
	cne = enc.encode('utf-8') #This is explicit encoding for utf, gets rid of a nasty ascii encoding error thrown by weird characters in the response text
	f.write(cne)
	f.close()
	
	#Time to sleep in between pull requests. Program seems to return errors if running with an interval less than 50 seconds. 
	#Recommend at least 5 minute intervals to avoid getting errors from Facebook
	time.sleep(300)
	pullcount +=1
	
