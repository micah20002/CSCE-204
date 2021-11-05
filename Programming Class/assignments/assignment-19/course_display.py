#author Micah Lee
def get_courses():
    courses = {}
    with open("assignments/assignment-19/courses.txt", "r") as file:
        for line in file:
            data = line.split(":")
            code = data[0].strip()
            class_name = data[1].strip()
            courses[code] = class_name
    return courses

def display_courses(courses):
    for key, value in courses.items():
        print(f"{key}: {value}")

def display_description(courses):
    code = input("Enter course code: ").strip().lower()
    if code in courses:
        print(courses[code])
    else:
        print(f"Sorry, \"{code}\" is not in our system.")


def main():

    courses = get_courses()
    
    while True:
        command = input("(V)iew, (L)ookup or (Q)uit: ").lower()

        if command == "v":
            display_courses(courses)
        elif command == "l":
            display_description(courses)
        elif command == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid command.")

main()