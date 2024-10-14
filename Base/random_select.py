import random

class select_random():
    def first_name(self):
        first_names = ["John", "Alice", "Michael", "Emma", "David", "Sophia", "James", "Isabella","Robert", "Mia", "William", "Olivia", "Thomas", "Ava", "Charles", "Emily","Daniel", "Grace", "Matthew", "Lily"]

        first_name=random.choice(first_names)
        return(str(first_name))
    

    def last_name(self):
        last_names=["Smith", "Johnson", "Brown", "Williams", "Jones", "Garcia", "Miller", "Davis","Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee"]

        last_name=random.choice(last_names)
        return(str(last_name))