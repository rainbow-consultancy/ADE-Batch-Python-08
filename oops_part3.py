# super key-word

class Person: # Parent
    def __init__(self, name) -> None:
        self.name = name
        print("Person Constructor")
    
    def get_name(self):
        return f"This is from Person Class - {self.name}"


class Employee(Person): # Child
    def __init__(self, name, emp_id) -> None:
        super().__init__(name) # call's Person Construtor
        self.emp_id = emp_id
        print("Employee Constructor")

    def get_name(self):
        return super().get_name()


# e = Employee("Mahesh", 100)
# print(e.emp_id, e.name)
# print(e.get_name())


# Abstraction

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def Start(self):
        pass  # abc should not contain any logic

class Car(Vehicle):
    def Stop(self):
        print("Car has Stopped")

    def Start(self):
        print("Car has Started")


c = Car()
c.Stop()
c.Start()