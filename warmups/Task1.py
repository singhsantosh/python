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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

listOfTelephoneNumbers = []

for text in texts:
    if text[0] not in listOfTelephoneNumbers:
        listOfTelephoneNumbers.append(text[0])
    if text[1] not in listOfTelephoneNumbers:
        listOfTelephoneNumbers.append(text[1])

for call in calls:
    if call[0] not in listOfTelephoneNumbers:
        listOfTelephoneNumbers.append(call[0])
    if call[1] not in listOfTelephoneNumbers:
        listOfTelephoneNumbers.append(call[1])


print("There are {} different telephone numbers in the records.".format(str(len(listOfTelephoneNumbers))))
