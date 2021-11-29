from criminal import Criminal

def get_criminals():
    criminals = []

    with open("excercises/nov-16/criminals.txt") as file:
        for line in file:
            data = line.split(',')
            first_name = data[0].strip()
            last_name = data[1].strip()
            gender = data[2].strip().lower()
            crime_type = data[3].strip().lower()
            in_jail = get_bool(data[4].strip())
            description = data[5].strip()
            criminals.append(Criminal(first_name, last_name, gender, crime_type, in_jail, description))
    return criminals

def get_bool(data):
    if data.lower() == "true":
        return True
    else:
        return False

criminals = get_criminals()

print("Welcome to our criminal system")

while True:
    command = input("Would you like to (V)iew, (S)earch, or (Q)uit: ").strip().lower()

    if command == "q":
        break
    if command == "v":
        for criminal in criminals:
            criminal.display()
    elif command == "s":
        gender = input("Enter 'male' or 'female': ").strip().lower()
        crime_type = input("Enter 'robbery', 'assault', or 'murder': ").strip().lower()
        print("Criminals that match your criteria: ")
        for criminal in criminals:
            if criminal.is_match(gender, crime_type):
                criminal.display()
    else:
        print("Invalid command")

print("Goodbye")

    