assignments = float(input("Assignments"))
excercises = float(input("Excercises"))
midterm = float(input("Midterm: "))
final = float(input("Final: "))
ClassGrade = assignments *.55 +excercises * .15 +midterm * .15 +final *.15

print(f"Your class grade is {round(ClassGrade, 1)}%.")

if ClassGrade >=90:
    print("You earned an A")
elif ClassGrade >= 80:
        print("You earned a B")
elif ClassGrade >= 70:
        print("You earned a c")
elif ClassGrade >= 60:
        print("You earned a D")

        else:
            print("you earned an F")

            print(f "You earned a {letter}")