def get_mood(color):
    colors = ["red", "yellow", "blue", "green", "black", "purple", "pink"]
    moods = ["angry", "mellow", "sad", "happy", "scary", "royal", "fun"]

    for i in range(len(colors)):
        if(colors[i] == color.lower().strip()):
            return moods[i]
    return False

print("Mood Ring!!!!")

color = input("Enter color of ring: ").lower().strip()
mood = get_mood(color)

if mood == False:
    print(f"Sorry {color} is not in our valid color list")
else:
    print(f"You are feeling very {mood}")
