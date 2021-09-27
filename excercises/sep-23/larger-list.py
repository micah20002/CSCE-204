toys = ["doll", "rope", "truck", "car", "shovel"]
print("Welcome to our toy store")

while True:
    command = input("(V)iew, (A)dd, (R)remove, (Q)uit: ").lower().strip()

    if command == "q":
        break
    elif command == "v":
        for toy in toys:
            print(f"- {toy}")
    elif command == "a":
        toy = input("Enter toy: ")
        toys.append(toy)
    elif command == "r":
        toy = input("Enter toy: ")
        toys.remove(toy)
    else:
        print("Invalid command")

print("Goodbye")