"""
Read file into texts and calls.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# phoneToCallMap contains phone as key and total no of seconds spent by that phone as value
phoneToCallMap = {}

for call in calls:
    if call[0] not in phoneToCallMap:
        phoneToCallMap[call[0]] = call[-1]
    else:
        phoneToCallMap[call[0]] = str(int(phoneToCallMap[call[0]]) + int(call[-1]))
    if call[1] not in phoneToCallMap:
        phoneToCallMap[call[1]] = call[-1]
    else:
        phoneToCallMap[call[1]] = str(int(phoneToCallMap[call[1]]) + int(call[-1]))

phoneWithLongestTime = None
longestDuration = 0

for k, v in phoneToCallMap.items():
    if int(v) > int(longestDuration):
        longestDuration = v
        phoneWithLongestTime = k

print("{} spent the longest time, {} seconds, on the phone during September 2016."
      .format(phoneWithLongestTime, longestDuration))
