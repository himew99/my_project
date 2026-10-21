from datetime import date

class Person:
    """
    This is a class to create persons who has name, age, ethnicity
    """
    people_count=0

    def __init__(self, first_name,last_name,birthday,ethnicity,address):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday


        year,month,day=birthday.split('/')
        self.year=int(year)
        self.month=int(month)
        self.day=int(day)


        self.ethnicity = ethnicity
        self.addres = address
       
        Person.people_count+=1


    def full_name(self):
        return f'{self.first_name} {self.last_name}'


    def __str__(self):
        return f'name:{self.full_name()},age: {self.age()}, ethnicity:{self.ethnicity}'
    
    @classmethod 
    def population(cls):
        return f'people_count:{cls.people_count}' 

    def age(self):
                current_date=date.today()
                current_year=current_date.year
                current_month=current_date.month
                current_day=current_date.day
        
                years=current_year-self.year
                months=current_month-self.month
                days=current_day-self.day
        
                if days<0:
                    months-=1
                if months<0:
                    years-=1
                return years
            

    