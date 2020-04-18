seconds = int
seconds = input ('what is seconds: ')
day = int (seconds / 86400)
aHour = seconds - day * 86400
hour = int (aHour / 3600)
aMinute = aHour - hour * 3600
minute = int (aMinute / 60)
aSecond = aMinute - minute * 60
second = int (aMinute / 60)
pday = str (day)
phour = str (hour) 
pminute = str (minute)
psecond = str (second)
if hour < 10:
    phour = str (0) + str (hour)
if minute < 10:
    pminute = str (0) + str (minute)
if second < 10:
    psecond = str (0) + str (second)
print (pday, phour, pminute, psecond, sep=':')