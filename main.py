from datetime import date


class Person:
    """A person with a name, birthday, ethnicity and address."""

    _people_count = 0

    def __init__(self, first_name, last_name, birthday, ethnicity, address):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday       
        self.ethnicity = ethnicity
        self.address = address          
        Person._people_count += 1

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
        return cls._people_count

    def __str__(self):
        return f'name: {self.full_name}, age: {self.age}, ethnicity: {self.ethnicity}'