#Author: Micah Lee

from job import Job

def get_jobs():
    jobs = []

    with open("assignments/assignment-24/jobs.txt") as file:
        for line in file:
            data = line.split('.')
            title = data[0].strip()
            description= data[1].strip()
            skills = data[2].strip().lower()
            length = data[3].strip().lower()
            pay = data[4].strip()
            jobs.append(Job (title, description, skills, length, pay))
    return jobs

def get_bool(data):
    if data.lower() == "true":
        return True
    else:
        return False

jobs = get_jobs()

print("Welcome to our job finder")

while True:
    command = input("(L)ist all jobs, get a jobs (D)etails, or (Q)uit: ").strip().lower()

    if command == "q":
        break
    if command == "l":
        for job in jobs:
            job.display()
    elif command == "d":
        title = input("Enter job name: ").strip().lower()
        for job in jobs:
            if job.is_match(title):
                job.display()
    else:
        print("Invalid command")

print("Goodbye")

    