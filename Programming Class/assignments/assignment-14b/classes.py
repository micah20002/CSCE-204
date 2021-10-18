# Author: Micah Lee
from datetime import date, time, datetime

mwclass = {
    "ITEC 265":datetime(2021, 10, 12, 00),
    "ITEC 101":datetime(2021, 10, 13, 10)}

tuethurclass = {
    "CSCE 204":datetime(2021, 10, 11, 00),
    "ITEC 233":datetime(2021, 10, 13, 15)}

for mwclas in mwclass:
    schedule = mwclass[mwclas]
    timeofclass= mwclass[mwclas]   
    if datetime.today().weekday() == 0:
        print(f"Your Classes Today: {mwclas} - " + timeofclass.strftime("%H %M %p"))

    elif datetime.today().weekday() == 1:
        print(f"Your Classes Today: {mwclas} - " + timeofclass.strftime("%H %M %p"))
    else:
        print("No Class Today!!")

for tuethurclas in tuethurclass:
    schedule = mwclass[mwclas]
    timeofclass= mwclass[mwclas]   
    if datetime.today().weekday() == 2:
        print(f"Your Classes Today: {tuethurclas} - " + timeofclass.strftime("%H %M %p"))

    elif datetime.today().weekday() == 3:
        print(f"Your Classes Today: {tuethurclas} - " + timeofclass.strftime("%H %M %p"))
    else:
        print("No Class Today!!")
