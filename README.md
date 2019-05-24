# Unscramble Computer Science Problem: Investigating Texts and Calls
by Mostafa Elsheikh, in fulfillment of Udacity's <i class="icon-cog"></i> **[Data Structures and Algorithms Nanodegree](https://www.udacity.com/course/nd256)**

## About

A project of five tasks based on a fabricated set of calls and texts exchanged during September 2016. Using Python to analyze and answer questions about the texts and calls contained in the dataset. Lastly, performing run time analysis of my solution and determine its efficiency.

## Getting Started

Under the folder investigate texts and calls you will find five python files `Task0.py` ~ `Task4.py` and in `_data` folder there are two csv files `calls.csv` and `texts.csv`.

### Data

The text and call data are provided in csv files. In each file, the data is already read and stored as lists of lists.

Each sub-list of the list of texts is structured in this way:
```
a text = [    Sending telephone number (string),
        receiving telephone number (string), 
        timestamp of text message (string)]
```

Each element in the list of phone calls is structured in this way:
```
a call = [    Calling telephone number (string), 
        receiving telephone number (string), 
        start timestamp of telephone call (string),
        duration of telephone call in seconds (string)]
```

## Tasks/Findings
### TASK 0:
What is the first record of texts and what is the last record of calls?
```
$ python Task0.py
First record of texts, 97424 22395 texts 90365 06212 at time 01-09-2016 06:03:22
Last record of calls, 98447 62998 calls (080)46304537 at time 30-09-2016 23:57:15, lasting 2151 seconds
```
### TASK 1:
How many different telephone numbers are there in the records? 
```
$ python Task1.py
There are 570 different telephone numbers in the records.
```
### TASK 2:
Which telephone number spent the longest time on the phone during the period? Don't forget that time spent answering a call is also time spent on the phone.
```
$ python Task2.py
(080)33251027 spent the longest time, 90456 seconds, on the phone during September 2016.
```
### TASK 3:
(080) is the area code for fixed line telephones in Bangalore. Fixed line numbers include parentheses, so Bangalore numbers have the form (080)xxxxxxx.

```
$ python Task3.py
```
Part A: Find all of the area codes and mobile prefixes called by people in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.
```
The numbers called by people in Bangalore have codes: ['9036', '7406', '04344', '044', '9844', '9900', '080', '9740', '9738', '8151', '9008', '9035', '9526', '8431', '8714', '9241', '040', '9341', '9741', '9342', '8301', '9961', '022', '9019', '7829', '9343', '7813', '9845', '8152', '9400', '04546', '7795', '9242', '9448', '0821', '9656', '9449', '9742', '0471']
```

Part B: What percentage of calls from fixed lines in Bangalore are made to fixed lines also in Bangalore? In other words, of all the calls made from a number starting with "(080)", what percentage of these calls were made to a number also starting with "(080)"?
```
24.81 percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.
```

The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.
```
$ python Task4.py
These numbers could be telemarketers: ['(022)37572285', '(022)65548497', '(022)68535788', '(022)69042431', '(040)30429041', '(044)22020822', '(0471)2171438', '(0471)6579079', '(080)20383942', '(080)25820765', '(080)31606520', '(080)40362016', '(080)60463379', '(080)60998034', '(080)62963633', '(080)64015211', '(080)69887826', '(0821)3257740', '1400481538', '1401747654', '1402316533', '1403072432', '1403579926', '1404073047', '1404368883', '1404787681', '1407539117', '1408371942', '1408409918', '1408672243', '1409421631', '1409668775', '1409994233', '74064 66270', '78291 94593', '87144 55014', '90351 90193', '92414 69419', '94495 03761', '97404 30456', '97407 84573', '97442 45192', '99617 25274']
```
