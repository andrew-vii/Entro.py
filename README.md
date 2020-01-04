# Entro.py
Facebook OSINT Collection and Analysis Tool

[Website Writeup](https://andrew-vii.github.io/entropy/)


Entro.py is a weekend project I made over a bet with a friend. It's designed to scrape Facebook chat statuses for active/last active time status, then output them to a (very basic) graph for an individual UID, resulting in a very accurate activity graph for a given user. Because Facebook leaks the last-active status for its chat users, you can get a fairly active picture of when someone is awake/asleep/at work, if they check Facebook at least a few times a day. 


There's three main parts to the application:

Puller: Scrapes Facebook chat status data. Requires a valid Facebook cookie to authenticate. Code is self-correcting for most errors that I encountered with automating the web requests, and the interval can be adjusted.

Organizer: Run this after puller is run for a decent length of time (I ran a few intervals of 5-10 days). Organizer sorts the individual pullcap files that puller.py outputs into the necessary directory structure for the analyer. It may take some customization based on your specific directory structure. 

Analyzer: Outputs a very basic graph for a specific UID, based on the information scraped through the puller program, and organized in the organizer program. Analyzer.py requires that organizer.py is run first.



This is very much a hacked-together solution and is not even close to production-quality code, so use at your own risk. 
