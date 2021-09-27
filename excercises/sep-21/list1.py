toys = ["car", "truck", "doll", "elmo", "yo-yo"]

print("My toy store")

toys.append("slinky") #used to add to the end of a list

#loop all toys in to a list
for i in range(len(toys)): # use the "length" function to loop for all items inside of list instead of hardcoded value
   print(f"({i+1}.{toys[i]}")

# for each loop

#for toy in toys: # !!uses the variable set (in this case toys) to loop all items in list
 #   print(toy)