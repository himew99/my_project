class Person:
    """
    This is a class to create persons who has name, age, ethnicity

    """
    people_count=0

    def __init__(self, first_name,last_name, age,ethnicity):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.ethnicity = ethnicity
        Person.people_count+=1

        print(f'"{self.first_name+' '+self.last_name}" has added sucsesfully')
        print('_'*50)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'name:{self.full_name()}, age:{self.age}, ethnicity:{self.ethnicity}'

    def population():
        return Person.people_count


