import random
print("Fortune Teller")

while True: # while true is an infinate loop until broken
    question = input("Enter question: ")
    num = random.randint(1,3)

    if num == 1:
        print("Yes")
    elif num == 2:
        print("No")
    elif num == 3:
        print("Maybe")

    playAgain = input("Do you want to play again? (Y)es or (N)o: ").strip().lower()

    if playAgain != "y":
        break # kicks you out of the while true loop

print("Goodbye")