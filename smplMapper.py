#!/usr/bin/env python
 
import sys
 
# input comes from STDIN (standard input)
for line in sys.stdin:
    try: #sometimes bad data can cause errors use this how you like to deal with lint and bad data
         
        personName = "-1" #default sorted as first
        personType = "-1" #default sorted as first
        countryName = "-1" #default sorted as first
        country2digit = "-1" #default sorted as first
         
        # remove leading and trailing whitespace
        line = line.strip()
         
        splits = line.split("|")
         
        if len(splits) == 2: #country data
            countryName = splits[0]
            country2digit = splits[1]
        else: #people data
            personName = splits[0]
            personType = splits[1]
            country2digit = splits[2]          
         
        print '%s^%s^%s^%s' % (country2digit,personType,personName,countryName)
    except: #errors are going to make your job fail which you may or may not want
        pass