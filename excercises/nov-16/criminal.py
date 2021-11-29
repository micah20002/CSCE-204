class Criminal:
    def __init__(self, first_name, last_name, gender, crime_type, in_jail, description):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.crime_type = crime_type
        self.in_jail = in_jail
        self.description = description

    def is_match(self, gender, crime_type):
        if self.in_jail == True:
            return False

        if gender == self.gender and crime_type == self.crime_type:
            return True

        return False

    def display(self):
        jail_desc = "not incarcerated"

        if self.in_jail == True:
            jail_desc = "Incarcerated"
        print(f"""
        {self.first_name} {self.last_name}
        Gender: {self.gender}
        Crime: {self.crime_type}
        {jail_desc}
        {self.description}         
            
""")