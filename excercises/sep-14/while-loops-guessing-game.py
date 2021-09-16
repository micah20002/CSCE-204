import random


goal = random.randint(1,100)

print("Computer number {goal}")

print("Welcome to our guessing game!")
guess = int(input("Enter a number between 1 and 100: "))
counter =1 

while guess != goal:
    print(f"Sorry, {guess} was not the answer!")

    if guess > goal:
        print("Too High!")
    else:
        print("Too low!")

    guess = int(input("Try again? "))
    counter +=1

print(f"Yay! You got it in {counter} tries!")