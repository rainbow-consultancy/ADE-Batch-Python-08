# list & tuple indexing
# Both list & tuple are iterables in python. So it supports indexing.

nums = [1, 2, 3, 4, 5]
print(nums[0])

print(nums[0:3])
print(nums[-1:-4:-1])

chars = ['a', 'b', 'c', 'd', 'e']
print(chars[::2]) # [a, c, e]

my_tup = ('a', 'b', 'c', 'd', 'e')
print(my_tup[::3])

print(my_tup[::])

# "abcde"
print("".join(my_tup))

# "a-b-c-d-e"
print("-".join(my_tup))


names = ["Python", "is", "awesome"]
print(" ".join(names))

