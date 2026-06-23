# sets - functions & behaviour (mutable & unorderd)

numbers = {1, 2, 3, 4, 5, 2, 3, 2, 3}
nums = {9, 8, 7, 2}

# add a single value to the set - add()
numbers.add(10)
# print(numbers)

# remove element - remove()
numbers.remove(3)
# print(numbers)

# remove random element - pop()
numbers.pop()
# print(numbers)

# remove all the elements - clear()
# numbers.clear()
# print(numbers)

# merge 2 sets together
result = numbers.union(nums)
# print(result)


# intersection - common elements between 2 sets
# print(numbers.intersection(nums))


# dictionaries - functions & behaviour (key:value pairs | mutable)
stu_info = {
    "stu_id": 123,
    "stu_name": "Prakash",
    "grade": 6
}

print(stu_info)

# add a element
stu_info["stu_city"] = "Bangalore"
print(stu_info)

# remove a element
stu_info.pop("grade")
print(stu_info)

print(stu_info["stu_name"])

print(stu_info.get("stu_name"))
