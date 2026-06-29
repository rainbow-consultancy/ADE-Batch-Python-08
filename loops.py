# loops in python

# Types Of Loops

# 1. for loop
# 2. while loop

# syntax of for loop

# approach - 1
# for var in iterable:  -- list, tuple, string, dict
#     code

# approach - 2
# for var in range(start, stop, step=1):
#     code


# approach - 1 example

# You have a list of nums, find the sqaure roots of each num inside the list and return the output list

nums = [1, 2, 3, 4, 5]  # input
# expected output = [1, 4, 9, 16, 25]
result = []

# for i in nums:
#     result.append(i**2)

# print(result)

# approach - 2

# for i in range(0, len(nums)):
#     result.append(nums[i]**2)
    
# print(result)

# for i in range(101):
#     print(i)
    

# name = "python"
# for i in name:
#     print(i)

# stu_info = {"stu_id": 100, "stu_name": "Harish", "grade": 9}

# for key, value in stu_info.items():
#     print(key, value)

# for key in stu_info.keys():
#     print(key)

# for value in stu_info.values():
#     print(value)


# 2. while loop - it is dangerous if you don't handel it well

# syntax 

# while condition:
#     code

# i = 1
# while i <= 10:
#     print(i)
#     # i = i+1 
#     i += 1  # pythonic way of value increment

# n = len(nums)
# i = 0
# result = []
# while i < n:
#     result.append(nums[i]**2)
#     i = i+1

# print(result)