print("Football favs")
teams = ["The Saints", "Ravins", "The Washington Football Team", "49ers", "Giants"]

for football in teams:
   print(f" - {football}")

while True:
      cont = input("Do you want to remove any teams?").strip().lower()
      if cont != "y":
         break
      teamName = input("Enter Team Name: ")
      teams.remove(teamName)

print("Goodbye")


# append homework assignments to homework list assignment