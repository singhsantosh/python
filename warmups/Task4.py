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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

telemarketers = []
othersMap = {}
callersMap = {}

for call in calls:
    callersMap[call[0]] = 'callers'
    othersMap[call[1]] = 'others'

for text in texts:
    othersMap[text[0]] = 'others'
    othersMap[text[1]] = 'others'


for ph in callersMap.keys():
    if ph not in othersMap:
        telemarketers.append(ph)

print("These numbers could be telemarketers: ")

for ph in sorted(telemarketers):
    print(ph)
