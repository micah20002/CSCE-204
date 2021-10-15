def factorial():
    num = int(input("Enter number: "))
    answer = 1

    if num <1:
        print("Invalid input")
        return

    #5! = 1 * 2 * 3 * 4 * 5
    for i in range(1, num + 1):
        answer *= i

        print(f"{num}! = {answer}")

def sum():
    num = int(input("Enter number: "))
    answer = 0

    if num < 1:
        print("Invalid input")
        return
        # sum of 4 = 1 + 2 + 3 +4
    for i in range(num+1):
            answer += i

    print(f"Sum of 1 to {num} = {answer}")


def power():
    base = int(input("Enter base: "))
    exponent = int(input("Enter exponent: "))
    answer = 1

    if base < 1 or exponent < 1:
        print("Invalid input")
        return

    # base 2 exponent is 3  = 2 * 2 * 2 =8
    for i in range(exponent):
        answer *= base

    print(f"{base} to the power of {exponent} = {answer}")

while True:
    command = input("Compute (F)actorial, (S)um, (P)ower, or (Q)uit")

    if command == "q":
        break
    elif command == "f":
        factorial()
    elif command == "s":
        sum()
    elif command =="p":
        power()
    else:
        print("Invalid command")

print("goodbye")