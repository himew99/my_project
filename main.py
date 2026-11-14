from datetime import date
from abc import ABCMeta,abstractmethod


class Person(metaclass=ABCMeta):
    """A person with a name, birthday, ethnicity and address."""

    people_count = 0

    def __init__(self, first_name, last_name, birthday, ethnicity, gender, address):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.ethnicity = ethnicity
        self.gender = gender
        self.address = address
        Person.people_count += 1

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, value):
        if isinstance(value, str):
            try:
                year, month, day = map(int, value.split('/'))
                value = date(year, month, day)
            except ValueError:
                raise ValueError('birthday must be a valid "YYYY/MM/DD" date')
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

    @property
    @abstractmethod
    def role(self):
        """ returns the type of person """
        pass

    @abstractmethod
    def details(self):
        """returns the new details of each object """


class Employee(Person):
    employee_count = 0

    def __init__(self, first_name, last_name, birthday, ethnicity, gender, address, job, salary):
        self.job = job
        self.salary = salary
        super().__init__(first_name, last_name, birthday, ethnicity, gender, address)
        Employee.employee_count += 1

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if isinstance(new_salary, bool) or not isinstance(new_salary, int):
            raise TypeError('salary must be an integer')
        if new_salary <= 0:
            raise ValueError('salary must be positive')
        self.__salary = new_salary

    def __str__(self):
        person_str = super().__str__()
        return f'{person_str} job:{self.job},salary:{self.salary} IQD'

    @staticmethod
    def iqd_to_usd(money, rate=1515):
        if isinstance(money, bool) or not isinstance(money, (int, float)):
            raise TypeError('money must be a number')
        return money / rate
    @classmethod
    def get_employee_num(cls):
        return cls.employee_count
    @property
    def role(self):
        return 'Employee'
    def details(self):
        return f'job:{self.job},salary:{self.salary}IQD'

class Student(Person):
    student_count=0
    def __init__(self, first_name, last_name, birthday, ethnicity, gender, address, education, studying_place):
        self.education = education
        self.studying_place = studying_place
        super().__init__(first_name, last_name, birthday, ethnicity, gender, address)
        Student.student_count+=1

    def __str__(self):
        person_str = super().__str__()
        return f'{person_str},education:{self.education} student on {self.studying_place}'

    @property
    def studying_place(self):
        return self.__studying_place

    @studying_place.setter
    def studying_place(self, place):
        if not isinstance(place, str):
            raise TypeError('studying_place must be a string')
        self.__studying_place = place
    @classmethod
    def st_count(cls):
        return cls.student_count

    @property
    def role(self):
        return 'Student'

    def details(self):
         return f'education: {self.education}, studying at: {self.studying_place}'