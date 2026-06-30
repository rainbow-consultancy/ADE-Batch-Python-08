# nested functions

from typing import Iterable


def outer_func():
    def inner_func():
        print("inner function")
    inner_func()  # call inner function
    print("outer function")


# outer_func()

# inner_func()


def calculate():
    def square(n):
        return n**2
    result = square(5)
    print(result)

# calculate()

# square(3)


# lambda functions - single line functions

# syntax 
# lambda arguments: code expressions

# def square(n):
#     return n**2 

# print(square(5))
# print(square(3))

square = lambda x: x**2
# print(square(4))
# print(square(5))
# print(square(3))

# find the maximum btw 2 numbers

get_max = lambda x, y: x if x > y else y
# print(get_max(20, 50))
# print(get_max(67, 23))

# find even numbers

is_even = lambda x: x%2 == 0
# print(is_even(12))
# print(is_even(9))


# -> given a list of numbers, find the sqaure roots of each number 
# input - [1,2,3,4,5]
# expec-output -> [1,4,9,16,25]

# Iterables -> str, list, tuple

# map() is used to apply a func to each value in a iterable datatype
# map(func, iterable)

input = [1, 2, 3, 4, 5]
# get_squares = list[int](map(lambda x: x**2, input))
# print(get_squares)

# filter() 
# filter(func, iterable)
res = list[int](filter(is_even, input))
print(res)


res = list[int](map(is_even, input))
print(res)
