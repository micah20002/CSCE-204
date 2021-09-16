# starting num.| end num. | loop by num. | can add a negative sign to loop by num to count downwards
#for i in range(10,1,-1):
#    print(i)


# _________________________________________

# loop from 1 - 10 and present sum
# sum = 0

# for i in range(1,10):
#    sum += i

#print(sum)

# _________________________________________


# ask the user for a number, if it is <1,
# give them an error
# then loop through and calculate the sum 1... usernum

usernum = int(input("Pick a number: "))

if usernum <1:
    print("Sorry, your number must be greater than 1")
else: 
    sum = 0

    for i in range(1, usernum +1):
        sum += i

    print(sum)