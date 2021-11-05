toys = {
    "doll":10.99,
    "truck": 5.60,
    "car": 3.50,
    "book": 7.20
    }

toys["unicorn"] = 9.60

# display our toys
for toy in toys:
    print(f"{toy}: ${toys[toy]}")

toy = input("Enter Toy: ")
print(f"{toy} costs ${toys[toy]}")