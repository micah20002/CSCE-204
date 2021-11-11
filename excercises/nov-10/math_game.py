import random

def get_score():
    with open("excercises/nov-10/score.txt") as file:
        lines = file.readlines()
        if not lines:
            return 0
        return int(lines.pop())

def save_score(score):
    with open("excercises/nov-10/score.txt", "w") as file:
        file.write(f"{score}")

def play_round():
    randNum = random.randint(1000,9999)
    sum = sum_digits(randNum)

    userAnswer = int(input(f"Sum of digits in {randNum}: "))

    if userAnswer == sum:
        return True
    else:
        print(f"Incorrect, answer should be {sum}")
        return False

def sum_digits(number):
    sum = 0
    while number > 0:
        digit = number % 10
        sum += digit
        number = number // 10
    return sum


print("Welcome to our Addition Game")
score = get_score()

while True:
    command = input("(P)lay or (Q)uit: ").strip().lower()

    if command == "q":
        break
    elif command !="p":
        print("Invalid Command")
        continue

    if play_round():
        score += 1
        print("Yay, you got it!")

    print(f"Your current score is {score}")

print("Goodbye")
save_score(score)
