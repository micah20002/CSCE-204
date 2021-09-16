import random
continue_check = "y"

print("Welcome to our Simple Math Game")

while(continue_check == "y"):

    num1 = random.randint(10,99)
    num2 = random.randint(10,99)

    guess = int(input(f"{num1}+{num2} = "))
    answer_check = num1 + num2

    if(guess == answer_check):
        print("Correct!")
    else:
        print(f"Sorry, the correct answer is {answer_check}")

    continue_check = input("Would you like to play again? (Y)es or (N)o: ") 

print("Goodbye")