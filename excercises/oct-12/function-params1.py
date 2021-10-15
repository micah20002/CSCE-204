def factorial(num):
    answer = 1

    if num < 0:
        print("Invalid number")
        return

        for i in range(1, num + 1):
            answer *= i

        print(f"{num}! = {answer}")

factorial(7)