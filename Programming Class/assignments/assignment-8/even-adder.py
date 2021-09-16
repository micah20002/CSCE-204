print("Welcome to our Even Number Adder")
end = int(input("Enter End Num: "))

counter = 2
sum = 0
 
for num in range(2, end+1):

    if num % 2 == 0:
        print(counter)
        sum += counter
        counter += 2

print(f"Sum: {sum}")