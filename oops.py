# OOPS - Object Oriented Programming

# class - A class is like a blue-print

# syntax

# class Employee:
#     pass

# emp1 = Employee()
# emp2 = Employee()
# emp3 = Employee()

# class Employee:

#     def get_details(self, emp_id, name):
#         return f'Employee ID: {emp_id}\nEmployee Name: {name}\n'

# emp = Employee()
# emp1_details = emp.get_details(100, "Lokesh")
# emp2_details = emp.get_details(200, "Pawan")

# print(emp1_details)
# print(emp2_details)


# Construtor Method


# class Employee:

#     def __init__(self, emp_id, name, salary):
#         self.emp_id = emp_id
#         self.name = name
#         self.salary = salary

#     def get_details(self):
#         return f"Employee ID: {self.emp_id}\nEmployee Name: {self.name}\nEmployee Salary: {self.salary}"

# emp1 = Employee(100, 'Rohith', 70_000)
# emp2 = Employee(200, 'Gagan', 40_000)

# print(emp1.get_details())
# print(emp2.get_details())

class Employee:
    global company
    company = "QuantCloud123"

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def get_details(self):
        my_public_var = "hello"
        return f"Employee ID: {self.emp_id}\nEmployee Name: {self.name}\nEmployee Salary: {self.salary}"

# emp = Employee(100, 'Rohith', 70_000)
# print(emp.company)
# print(emp.emp_id)
# print(emp.my_private_var)

# print(company)


# Global variable - A global variable can be used any where in the code.
# Public Variable - A public variable is confined to its fence, either inside a function or a class. 
# You'll be able to access it with in its scope only

# Private Variable - This is a restricted variable, secured variable you can't access it outside the class.

# __name = "Kalyan"  -- this is how we define a private variable


class BankAccount:
    def __init__(self, acct_holder, balance) -> None:
        self.acct_holder = acct_holder
        self.__balance = balance # private var

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
    
    def get_balance(self):
        return self.__balance

acct = BankAccount("Mahesh", 5000)

acct.deposit(5000)
acct.withdraw(2000)

print(acct.get_balance())
print(acct.acct_holder)
print(acct.__balance)
