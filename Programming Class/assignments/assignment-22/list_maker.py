# Author: Micah Lee

FILE_NAME = "assignments/assignment-22/santas_list.txt"
def write_toys(toys):
    with open(FILE_NAME, "w") as file:
        for toy in toys:
            file.write(toy + "\n")

def read_toys():
    toys = []
    with open(FILE_NAME) as file:
        for line in file:
            line = line.replace("\n","").strip()
            toys.append(line)
    return toys

def list_toys(toys):
    for i in range(len(toys)):
        print(f"- {toys[i]}")

def add_toy(toys):
    toy = input("toy: ").strip()
    toys.append(toy)
    write_toys(toys)
    print(f"{toy} was added.")
    return toys

def delete_toy(toys):
    index = input("Enter toy name: ")

    if index != len(toys):
        write_toys(toys)
        print(f" {toys} was deleted.")
    else:
        print(f"Sorry, toy is not on the list.")
    return toys

while True:
    command = input("Enter (L)ist, (A)dd, (D)elete, or (Q)uit: ").lower().strip()
    toys = read_toys()

    if command == "l":
        list_toys(toys)

    elif command == "a":
        books = add_toy(toys)
    
    elif command == "d":
        books = delete_toy(toys)

    elif command == "q":
        break
    else:
        print("Invalid command, try again.")

print("Goodbye")