#Author: Micah Lee

class Job:
    def __init__(self, title, description, skills, length, pay):
        self.title = title
        self.description = description
        self.skills = skills
        self.length = length
        self.pay = pay

    def is_match(self, title):
        if self.title == True:
            return False

        if title == self.title:
            return False

        return True

    def display(self):

        print(f"""\n
*** {self.title} ***
{self.description}
Skills:\n- {self.skills}    
Contract Length: {self.length} 
Pay rate: {self.pay} yearly   
            
""")