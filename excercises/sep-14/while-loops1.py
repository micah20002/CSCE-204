command = input("Do you want to say hello? (Y/N)").lower().strip()

while command == "y" :
    print("Hello!")
    command = input("Do you want to say hello again?")

print("Goodbye")