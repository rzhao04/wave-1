day = int
day = input ('what is day: ')
dayInSec = day * 86400
hour = int
hour = input ('what is hour: ')
hourInSec = hour * 3600
minute = int
minute = input ('what is minute: ')
minuteInSec = minute * 60
second = int
second = input ('what is second: ')
seconds = dayInSec + hourInSec + minuteInSec + second
print (seconds)