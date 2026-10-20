class Person:
    """
    This is a class to create persons who has name, age, ethnicity

    """
    people_count=0

    def __init__(self, first_name,last_name,birthday,ethnicity,address):
        self.first_name = first_name
        self.last_name = last_name
        b_year,b_month,b_day=birthday.split('/')
        self.b_year=int(b_year)
        self.b_month=int(b_month)
        self.b_day=int(b_day)
        self.ethnicity = ethnicity
        governorate, neighborhood,house_number=address.split('/')
        self.governorate=governorate
        self.neighborhood=neighborhood
        self.house_n=house_number


        Person.people_count+=1

        print(f'"{self.first_name+' '+self.last_name}" has added sucsesfully')
        print('_'*50)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_birth(self):
        return f'{self.b_year}/{self.b_month}/{self.b_day}'

    def __str__(self):
        return f'name:{self.full_name()}, ethnicity:{self.ethnicity},Birth:{self.get_birth()}'
    
    @classmethod 
    def population(cls):
        return f'people_count:{cls.people_count}' 