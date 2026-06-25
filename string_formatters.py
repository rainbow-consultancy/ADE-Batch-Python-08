# string-formatters

name1 = input("Enter name1: ")
name2 = input("Enter name2: ")
# message = "Hey, good morning " + name
# print(message)

# 1. method1 - .format()

message = "Hey, good morning {0} and {1}".format(name1, name2)
# print(message)

message = "Hey, good morning {var1} and {var2}".format(var1=name1, var2=name2)
# print(message)

# 2. method2 - short hand notation - f""

message = f"Hey, good morning {name1} and {name2}"
print(message)




