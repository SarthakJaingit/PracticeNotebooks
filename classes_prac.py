#Python Object - Oriented Programming

class Employee:

    #Class states tend to be same for all instances
    num_of_employees = 0
    raise_amount = 1.5
    company_raise_money = 0

    def __init__(self, first, last, pay):
        #States
        #attributes initiliazed when making a new instance
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_employees += 1

    #Methods that you can do to the Employee Data Structure
    #Regular methods change the data of the instance itself

    #functions that calculate a new attribute based on previous initialized attributes
    @property
    def fullname(self):
        return (self.first + " " + self.last)

    @property
    def email(self):
        return self.first + "." + self.last+ "@gmail.com"

    #What happens when we use an equal sign to set a calculated attribute in our instance
    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split()

    # What happens when you use del on a calculated attribute in our instance.
    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None

    def apply_raise(self):
        original_pay = self.pay
        self.pay = int(self.pay * self.raise_amount)
        Employee.company_raise_money += (self.pay - original_pay)

    #Class methods involve changing the data of the class iteslf
    #Method helps alter class variables
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    #Method that helps in intilization of every instance
    @classmethod
    def from_string(cls, dash_string):
        first, last, pay = dash_string.split("-")
        return cls(first = first, last = last, pay = pay)

    # Don't use any class or instance data but just related to class
    @staticmethod
    def get_acquired(sell_amount):
        if sell_amount > 20000:
            print("We have been acquired")
        else:
            print("Nevermind")

    def __repr__(self):
        return "Employee({},{}, {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} {} : {}".format(self.first, self.last, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __mul__(self, other):
        return self.pay * other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee(first = "Sarthak", last = "Jain", pay = 100)
emp_2 = Employee(first = "Guy", last = "Montag", pay = 150)


emp_1.fullname = "Johny Test"
print(str(emp_1.fullname))
print(str(emp_1.first))

del emp_1.fullname
print(emp_1.first)




# emp_1.first = "Billy"
# print(emp_1.email)
# print(emp_1.fullname)

# print(emp_2)
# print(len(emp_2))
# print(emp_1  * emp_2)
# print(emp_1 + emp_2)
# print(emp_1)
# print(emp_2)
# print(repr(emp_1))

class Developer(Employee):

    raise_amount = 2

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.proglang = prog_lang

    @classmethod
    def from_string(cls, dash_string):
        first, last, pay, language = dash_string.split("-")
        return cls(first = first, last = last, pay = pay, prog_lang = language)

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = list()
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employee(self):
        for employee in self.employees:
            print("--> {}".format(employee.fullname()))



dev_1 = Developer("John", "Doe", 2000, "Java")
dev_2 = Developer("Mike", "James", 3000, "Python")
dev_3 = Developer.from_string("Micheal-Jackson-1500-Java")

mgr_1 = Manager("Sue", "Smith", 90000, [dev_1, dev_3])

# print(issubclass(Manager, Employee))
# print(issubclass(Manager, Developer))
#
# print(isinstance(mgr_1, Employee))
# print(isinstance(dev_1, Manager))


# print(mgr_1.email)
# mgr_1.add_employee(dev_2)
# mgr_1.print_employee()
# print("\n")
# mgr_1.remove_employee(dev_3)
# mgr_1.print_employee()

# print(dev_1.fullname())
# print(dev_2.email)
# print(dev_2.proglang)
# print(Developer.raise_amount)
# print(dev_1.raise_amount)

#emp_1 = Employee(first = "Sarthak", last = "Jain", pay = 100)
# emp_2 = Employee(first = "Guy", last = "Montag", pay = 100)
#
# emp_1.get_acquired(20000000)


# emp_str_1 = "John-Doe-2000"
# emp_str_2 = "Jane-Doe-1500"
#
# new_emp_1 = Employee.from_string(emp_str_2)
# print(new_emp_1.pay)
# print(new_emp_1.first)
# print(new_emp_1.last)


# Employee.set_raise_amount(1.05)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
#
# print(emp_1.raise_amount)
# emp_1.apply_raise()
# emp_2.apply_raise()
#
# print(emp_1.pay)
# print(emp_2.pay)

# print(emp_1.company_raise_money)
# print(emp_2.company_raise_money)
