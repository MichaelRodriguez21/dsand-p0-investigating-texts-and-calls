"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from datetime import datetime
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
# initalizing a tuple of three items (telephone number, call duration, start of telephone call)
longest_call = (calls[0][1], int(calls[0][3]), calls[0][2])

for call in calls:
    if longest_call[1] < int(call[3]):
        longest_call = (call[1], int(call[3]), call[2])

telephone_formatted_date = datetime.strftime(datetime.strptime(longest_call[2], '%d-%m-%Y %H:%M:%S'), '%B %Y')
print("{} spent the longest time, {} seconds, on the phone during {}.".format(longest_call[0], longest_call[1], telephone_formatted_date))
