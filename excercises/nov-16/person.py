class Person:
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def display(self):
        print(f"Hello {self.first_name} {self.last_name}: {self.phone_number}")