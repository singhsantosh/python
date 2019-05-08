"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
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
others = []
callers = []

for call in calls:
    if call[0] not in callers:
        callers.append(call[0])
    if call[1] not in others:
        others.append(call[1])

for text in texts:
    if text[0] not in others:
        others.append(text[0])
    if text[1] not in others:
        others.append(text[1])

for ph in callers:
    if ph not in others:
        telemarketers.append(ph)

print("These numbers could be telemarketers: ")

for ph in telemarketers:
    print(ph)
