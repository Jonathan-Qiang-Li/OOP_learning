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
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # ===================== These are Static methods ==================================#
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# ===================== Create subclass Developer ==================================#
# inheritance from employee class
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # below are instance variables, self is instance
        super().__init__(first, last, pay)  # use the logic from parent employee
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


emp_1 = Employee('Jon', 'Snow', 5000)
emp_2 = Employee('Test', 'User', 4000)

dev_1 = Developer('Jon', 'Snow', 5000, 'Python')
dev_2 = Developer('Test', 'User', 4000, "Java")

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.print_emps()

print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))

#
# import datetime
#
# my_date = datetime.date(2016, 7, 10)
#
# print(Employee.is_workday(my_date))
#
# emp_str_1 = 'John-smith-7000'
# emp_str_2 = 'Stevev-Seven-5000'
# emp_str_3 = 'James-Black-6000'
#
# new_emp_1 = Employee.from_string(emp_str_1)
#
# print(Employee.raise_amount)
# # class method change raise
# Employee.set_raise_amt(1.05)
# print(Employee.raise_amount)
#
# print(Employee.num_of_emps)
# print(emp_1.__dict__)
#
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
#
# print(emp_1)
# print(emp_2)
#
# print(emp_1.email)
# print(emp_2.email)
#
# # those are the same
# print(Employee.fullname(emp_1))
# print(emp_1.fullname())
