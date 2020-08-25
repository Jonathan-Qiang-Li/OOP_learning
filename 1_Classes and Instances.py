# Python Object-Oriented Programming from Corey Schafer
# youtube: https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

class Employee:
    # These are class variables
    num_of_emps = 0
    raise_amount = 1.04

    # ===================== These are INstance methods ==================================#
    def __init__(self, first, last, pay):
        # below are instance variables, self is instance
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # Note Employee.raise_amount change raise for all employee
        # Self.raise_amount raise for instance (unique) employee
        self.pay = int(self.pay * self.raise_amount)

    # ===================== These are Class methods ==================================#
    # decorator
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str_1.split('-')
        return cls(first, last, pay)
    # ===================== These are Static methods ==================================#
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True




emp_1 = Employee('Jon', 'Snow', 5000)
emp_2 = Employee('Test', 'User', 4000)

import datetime
my_date = datetime.date(2016,7,10)

print(Employee.is_workday(my_date))


emp_str_1 = 'John-smith-7000'
emp_str_2 = 'Stevev-Seven-5000'
emp_str_3 = 'James-Black-6000'

new_emp_1 = Employee.from_string(emp_str_1)

print(Employee.raise_amount)
# class method change raise
Employee.set_raise_amt(1.05)
print(Employee.raise_amount)

print(Employee.num_of_emps)
print(emp_1.__dict__)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_1)
print(emp_2)

print(emp_1.email)
print(emp_2.email)

# those are the same
print(Employee.fullname(emp_1))
print(emp_1.fullname())
