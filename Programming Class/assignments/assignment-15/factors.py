#Author: Micah Lee

def displayFactors():
    num = int(input("Enter number: "))
    answer = 1

    if num <1:
        print("Invalid input")
        return

    print('The factors of', num, 'are:')
    for i in range(1, num+1):
        if(num % i) == 0:
            print(i, end=' ')
    print("\n")

def isFactor():
    num = int(input("Enter number: "))
    factor = int(input("Potential Factor: "))
    answer = 0

    if num < 1:
        print("Invalid input")
        return

    if(num % factor == 0) :
        print(f"{factor} is a factor of {num}");
    else:
        print(f"{factor} is not a factor of {num}");

while True:
    command = input("(C)heck Factor, (L)ist factors, or (Q)uit: ")

    if command == "q":
        break
    elif command == "l":
        displayFactors()
    elif command == "c":
        isFactor()
    else:
        print("Invalid command")

print("goodbye")