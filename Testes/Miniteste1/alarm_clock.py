import datetime
time = datetime.datetime.now()
minute = (time.minute + 30)%60
hour = (time.hour + 8 + (time.minute + 30)//60)%24
a=(str(hour)+":"+str(minute))
print(a)
