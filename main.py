from datetime import date


class Person:
    """A person with a name, birthday, ethnicity and address."""

    people_count = 0

    def __init__(self, first_name, last_name, birthday, ethnicity, gender,address):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday       
        self.ethnicity = ethnicity
        self.gender=gender
        self.address = address          
        Person.people_count += 1

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, value):
        if isinstance(value, str):
            year, month, day = map(int, value.split('/'))
            value = date(year, month, day)      
        if not isinstance(value, date):
            raise TypeError('birthday must be a date or a "YYYY/MM/DD" string')
        if value > date.today():
            raise ValueError('birthday cannot be in the future')
        self.__birthday = value

    @property
    def age(self):
        today = date.today()
        had_birthday = (today.month, today.day) >= (self.__birthday.month, self.__birthday.day)
        return today.year - self.__birthday.year - (not had_birthday)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def population(cls):
        return cls.people_count

    def __str__(self):
        return f'name: {self.full_name}, age: {self.age}, ethnicity: {self.ethnicity}'

class Employee(Person):
    Empolyee_count=0

    def __init__(self, first_name, last_name, birthday, ethnicity, gender,address,job,salary):
        super().__init__(first_name, last_name, birthday, ethnicity, gender,address)
        self.job=job
        self.salary=salary
        Employee.Empolyee_count+=1

    

    @property
    def salary(self):
        return f'{self.__salary}'

    @salary.setter
    def salary(self,new_salary):
        if not isinstance(new_salary,int):
            raise TypeError('Salary must be an integer')
        elif not 0<new_salary<10000000:
            raise ValueError
        else:
            self.__salary=new_salary

    def __str__(self):
        person_str=super().__str__()
        return f'{person_str} job:{self.job},salary:{self.salary} IQD'
    
    @staticmethod
    def IQD_to_USD(money_in_IQD):
        if not isinstance(money_in_IQD,int):
            print('must be an integer')
        else:
            return money_in_IQD/1310

    @classmethod
    def get_employee_num(cls):
        return cls.Empolyee_count
