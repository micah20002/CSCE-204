from person import Person
"""
friend = Person("Sandra", "White", "803-322-6431")
friend.display()
friend2 = Person("Bobby", "White", "803-448-9439")
friend2.display()
"""



people = (
    Person("Sandra", "White", "803-322-6431"),
    Person("Bobby", "White", "803-448-9439"),
    Person("Kimmie", "White", "803-987-4170"),
    Person("Daniel", "White", "803-454-9977")
)

for person in people:
    person.display()