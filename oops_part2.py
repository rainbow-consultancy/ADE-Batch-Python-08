# OOPS 

# 1. Encapsulation
# 2. Polymorphism
# 3. Abstraction
# 4. Inheritance

# Encapsulation 

class BankAccount:
    def __init__(self, acct_holder, balance) -> None:
        self.acct_holder = acct_holder
        self.__balance = balance # private var

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
    
    def __get_balance(self): # private method
        return self.__balance

    def show_balance(self):
        return self.__get_balance()
    
# acct = BankAccount("Mahesh", 5000)
# print(acct.show_balance())

# 2. Inheritance

# Parent Class / Base Class
# Child Class / Derived Class

# 1. Single Inheritance

class Parent:
    name = "Parent"
    def properties(self):
        print("Hey, this is Parent Class Properties")


class Child(Parent):
    def info(self):
        print("This is a child class")


# c = Child()
# print(c.name)
# c.properties()
# c.info()

# 2. Multiple Inheritance

class Father:
    def get_father_props(self):
        print("Building")

class Mother:
    def get_mother_props(self):
        print("Jewlery & Farm House")

class Child(Father, Mother):
    def info(self):
        print("This is a child class")

# c = Child()
# c.get_mother_props()
# c.get_father_props()


# 3. Multi-level Inheritance

class GrandFather:
    def get_gf_props(self):
        print("Farm House")

class Father(GrandFather):
    def get_father_props(self):
        print("Building")

class Child(Father):
    def info(self):
        print("This is a child class")

# c = Child()
# c.get_gf_props()
# c.get_father_props()

# f = Father()
# f.get_gf_props()


# 3. Polymorphism - many forms

# method over-riding

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dogs Barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")


# d = Dog()
# c = Cat()

# d.sound()
# c.sound()

# method-overloading

def add(a, b):
    return a+b

def add(a, b, c):
    return a+b+c

# print(add(1,2,3))
# print(add(1,2))

def add(a, b, c=0):
    return a+b+c

# print(add(1,2,3))
# print(add(1,2))

