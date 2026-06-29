# function - A function is a re-usable block of code that can perform a specific task

# functions are of 2 types : 1. Built-in functions, 2. User-defined functions

# name = "python"
# print(name.upper())
# print(name.index('t'))

# User defined functions

a = 100
b = 300

# print(a + b)

c = 240
d = 540

# print(c + d)


# syntax
# def function_name():
#     code
#     return result


# static function
# def greet():
#     print("Hello, Good Morning!")

# greet()

# Dynamic Functions

# syntax
# def function_name(para1, para2):
#     code uses parameters
#     return result


# def add(x, y):
#     return x + y

# res1 = add(a, b)
# res2 = add(c, d)

# print(res1)
# print(res2)

# print(add(1, 30, 40, 50, 20))


# *args & **kwargs

def add(*nums):
    return sum(nums)

# print(add(1, 30, 40, 50, 20))
# print(add(1, 30))
# print(add(1, 30, 40))

def emp_details(**kwargs):
    print(kwargs)

print(emp_details(name="Jhon", age=30, city="Bangalore", state="Karnataka"))
