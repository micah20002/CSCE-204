from datetime import date, time, datetime
events = {"Classes Begin": date(2021, 8, 19),              "Add/Drop": date(2021, 8, 25),              "Labor Day Holiday": date(2021, 9, 6),              "Fall Break Day": date(2021, 10, 7),              "Last Day to Drop": date(2021, 11, 3),              "Thanksgiving": date(2021, 11, 25),              "Last Day of Class": date(2021, 12, 3),              "Reading Day": date(2021, 12, 4),              "Commencement": date(2021, 12, 13)}

counter = 1

for event in events:
    countDown = events[event]
    timeTill= events[event]
    daysTillEvent = (countDown - date.today()).days
    # if event is in next 30 days:
    if daysTillEvent < 30:
        print(f"{counter}. {event} - " + timeTill.strftime("%b %d, %A"))
        # if event is today
    
    elif daysTillEvent < 1:
        print(f"{counter}. {event} - " + timeTill.strftime("%b %d, %A"))

        # event is not today or within 30 days
    else:
        print(f"{counter}. {event} - " + timeTill.strftime("%b %d, %A"))
    
    counter += 1