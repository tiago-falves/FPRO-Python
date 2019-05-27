
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 11:57:34 2018

@author: Asus
"""
import datetime
now = datetime.datetime.now()
print()
print ("Time now: " + now.strftime("%H:%M"))
print()
print("The alarm will sound in 8 hours and 30 minutes.")
print()
alarm_time =(now + datetime.timedelta(hours=8, minutes = 30)).strftime("%H:%M")
print(str(alarm_time))