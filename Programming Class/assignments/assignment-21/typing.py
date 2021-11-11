import random
import string

def get_score():
    with open("assignments/assignment-21/score.txt") as file:
        lines = file.readlines()
        if not lines:
            return 0
        return int(lines.pop())

def save_score(score):
    with open("assignments/assignment-21/score.txt", "w") as file:
        file.write(f"{score}")

def play_round():
    for i in range(10):
        randLetter = random.choice(string.ascii_letters)

        userAnswer = str(input(f"{randLetter}: "))

    if userAnswer == randLetter:
        return True
    else:
        print(f"Incorrect, answer should be {randLetter}")
        return False

def display_scores(scores):
    score = get_score()    
    score += 1
    print("You won this round!")

    print(f"Your current score is {score}")


print("Lets Learn to Type")
score = get_score()

while True:
    command = input("(P)lay or (Q)uit: ").strip().lower()

    if command == "q":
        break
    elif command !="p":
        print("Invalid Command")
        continue

    if play_round():
        # make this count 1/10 instead of just constantly adding total
        score += 1
        print("You won this round!")

    print(f"Your current score is {score}")

print("Goodbye")
save_score(score)