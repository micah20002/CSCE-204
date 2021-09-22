print("Lets Configure Your Homework List")
homework = []


while True:
      homeworkItems = input("Enter Homework Item: ")
      homework.append(homeworkItems)

      cont = input("Would You Like to Add Another Item (Y)es or (N)o: ").strip().lower()
      if cont != "y":
         break
for work in homework:
   print(f" - {work}")


# toys.append("slinky")

# append homework assignments to homework list assignment