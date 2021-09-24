# Author: Micah Lee
companies = ("ScanSource", "Blackboard", "AVX", "3D Systems", "Life Cycle Engineering", "Palmetto", "Human Technologies", "O'Neal", "HKA Enterprises", "UC Synergetic")
wishList = []

while True:
    command = input("(V)iew, (A)dd company to wish list, (R)remove company from wishlist, (Q)uit: ").lower().strip()

    if command == "q":
        break
    elif command == "v":
        print("View (A)ll companies or your (W)ish List? ")
    elif command == "c":
            for work in companies:
                print(f"- {work}")
    elif command == "w":
            for wish in wishList:
                print(f"- {wish}")
    elif command == "a":
        wish = input("Enter Company: ")
        wishList.append(wish)
    elif command == "r":
        wish = input("Enter Company: ")
        wishList.remove(wish)
    else:
        print("Invalid command")


print("Goodbye")