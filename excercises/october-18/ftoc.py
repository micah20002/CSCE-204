def farh_to_cels(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def cels_to_fahr(celsius):
    fahrenheit = celsius * 9/5 +32
    return fahrenheit

def miles_to_kilo(miles):
    kilometers = miles * 1.60934
    return kilometers

def kilo_to_miles(kilo):
    miles = kilo * 0.621371
    return miles

print("Conversion Program")
command = int(input(f"""
Enter type of conversion:
1: Farenheit to celcius
2. celcius to farenheit
3. miles to kilometers
4. kilometers to miles
"""))

value = float(input("Enter value: "))

if command < 1 or command > 4:
    print("Sorry invalid command")
elif command == 1:
    result = farh_to_cels(value)
    print(f"{value}F = {round(result)}C")
elif command == 2:
    result = cels_to_fahr(value)
    print(f"{value}C = {round(result,2)}")
elif command == 3:
    result = miles_to_kilo(value)
    print(f"{value} miles = {round(result,2)} kilometers")
elif command == 4:
    result = kilo_to_miles(value)
    print(f"{value} kilometers = {round(result,2)} miles")
