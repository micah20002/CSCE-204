from datetime import date, time, datetime

birthdays = [date(2021, 3, 22), date(2021, 2, 10), date(2021, 5, 29),
             date(2021, 11, 21), date(2021, 10, 22), date(2021, 12, 12),
             date(2021, 6, 24)]

closestBirthday = date(2021, 12, 31)

for birthday in birthdays:
    daysTillBirthday = (birthday - date.today()).days
    daysTillCurrentClosest = (closestBirthday - date.today()).days
    # if birthday (date) already occured:
    if daysTillBirthday < 0:
        continue

    if daysTillBirthday < daysTillCurrentClosest:
        closestBirthday = birthday



print("The closest birthday is " + closestBirthday.strftime("%m/%d/%y"))
