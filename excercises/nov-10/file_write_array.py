friends = ["Amy", "Beth", "Carl", "Dave"]

with open("excercises/nov-10/friends.txt","w") as file:
    for friend in friends:
        file.write(f"{friend}\n")
