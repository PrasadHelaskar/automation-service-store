from Base.logfile import Logger
import random

log = Logger().get_logger()
class select_random():
    def first_name(self):
        first_names = ["John", "Alice", "Michael", "Emma", "David", "Sophia", "James", "Isabella", "Robert", "Mia", "William", "Olivia", "Thomas", "Ava", "Charles", "Emily", "Daniel", "Grace", "Matthew", "Lily", "Christopher", "Hannah", "Joseph", "Chloe", "Anthony", "Madison", "Andrew", "Ella", "Joshua", "Abigail", "Ethan", "Samantha", "Benjamin", "Natalie", "Alexander", "Zoe", "Jacob", "Elizabeth", "Ryan", "Victoria"]


        first_name=random.choice(first_names)
        return(str(first_name))
    

    def last_name(self):
        last_names = ["Smith", "Johnson", "Brown", "Williams", "Jones", "Garcia", "Miller", "Davis", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Clark", "Lewis", "Young", "Hall", "Allen", "Scott", "Wright", "King", "Green", "Adams", "Baker", "Nelson", "Hill", "Ramirez", "Campbell", "Mitchell", "Roberts", "Carter", "Phillips", "Evans"]


        last_name=random.choice(last_names)
        return(str(last_name))
    
    def random_month(self):
        months = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]

        month=random.choice(months)
        return(str(month))
    
    def random_year(self):
        years = [2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005]

        year=random.choice(years)
        return(year)
    
    def random_number(self, i):
        number=random.randint(1, i)
        # log.info(number)
        return number  