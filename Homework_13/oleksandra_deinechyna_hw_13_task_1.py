"""Сделать примеры в файлике. __call__ __repr__
@classmethod &@staticmethod
@property, setter, deleter"""


class Person:

    persons_counter = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        Person.persons_counter += 1

    def __call__(self):
        return f'Hi {self.first_name}!'

    def __repr__(self):
        return f'Person("{self.first_name}","{self.last_name}","{self.age}")'

    @staticmethod
    def is_adult(age):
        if age >= 18:
            return True
        else:
            return False

    @classmethod
    def total_persons(cls):
        return f'Total persons: {cls.persons_counter}'

    @property
    def age(self):
        return self.age_user

    @age.setter
    def age(self, value):
        self.age_user = value

    @age.deleter
    def age(self):
        self.age_user = 0


alex = Person('Alex', 'Smith', '39')
print(alex())  # using __call__
print(repr(alex))  # using __repr__
print(Person.is_adult(25))  # using @staticmethod

maria = Person('Mary', 'Jane', '25')
print(Person.total_persons())  # using @classmethod

print(alex.age)  # using getter
alex.age = 31  # using setter
print(alex.age)
del alex.age  # using deleter
print(alex.age)
