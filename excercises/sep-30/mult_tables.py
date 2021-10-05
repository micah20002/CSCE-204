"""
1 2 3
2 4 6
3 6 9
"""
endNum = int(input("Enter how many multiplication tables: "))

for row in range(1, endNum +1):
    #loop through columns
    for col in range(1, endNum +1):
        # if its a single digit
        if(len(str(row*col)) < 2):
            print(f" {row * col} ", end="")
        else:
            print(f"{row * col} ", end="") 
    print() # display a new line
