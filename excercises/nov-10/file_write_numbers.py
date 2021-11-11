numbers = [7,16,43,87]

with open("excercises/nov-10/numbers.txt", "w") as file:
    for number in numbers:
        file.write(str(number) + "\n")