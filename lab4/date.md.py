#1
import datetime

def subtract_five_days():
    current_date = datetime.datetime.now()
    five_days_ago = current_date - datetime.timedelta(days=5)
    return five_days_ago

print(subtract_five_days())


#2
# Write a Python program to print yesterday, today, tomorrow.
import datetime

def printYesterday():
    current_date = datetime.datetime.now()
    yesterday = current_date - datetime.timedelta(1)
    return yesterday

print(printYesterday())


def printToday():
    current_date = datetime.datetime.now()
    return current_date

print(printToday())


def printTomorrow():
    current_date = datetime.datetime.now()
    tomorrow = current_date + datetime.timedelta(1)
    return tomorrow

print(printTomorrow())


#3
import datetime

def delMicroSec(x):
    return x.replace(microsecond = 0)

current_datetime = datetime.datetime.now()
new_time = delMicroSec(current_datetime)

print(new_time)


#4
import datetime

def diffInSeconds(date1, date2):
    difference = date2 - date1
    differenceInSec = difference.total_seconds()
    return differenceInSec

# year - month - day - hour - minute - second
date1 = datetime.datetime(2019, 1, 1, 12, 0, 0)  
date2 = datetime.datetime(2024, 1, 1, 12, 0, 10)

difference_seconds = diffInSeconds(date1, date2)
print(difference_seconds)