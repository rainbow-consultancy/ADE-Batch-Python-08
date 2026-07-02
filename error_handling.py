# Error Handling or Exception Handling
# try & catch methods

# 1. syntax error
# 2. Run time errors
# 3. Logical errors

# print("Start")

# print(10/0)

# print("End")

# syntax

# try:
#     code logic
# except Exception:
#     message
# finally:
#     print("End")

# try:
#     print("Start")
#     print(10/0)
# except:
#     print("Can't divide by zero")
# finally:
#     print("End")

# num = int(input("Enter a number: "))


# try:
#     num = int(input("Enter a number: "))
#     print(100/num)
# except:
#     print("invalid input, expecting a valid non zero integer value.")

# try:
#     num = int(input("Enter a number: "))
#     print(100/num)
# except ZeroDivisionError:
#     print("Division by zero is not allowed")
# except ValueError:
#     print("Enter numbers only")


# try:
#     num = int(input("Enter a number: "))
#     print(100/num)
# except Exception as e:
#     print(e)

try:
    num = int(input("Enter a number: "))
    print(100/num)
except Exception as e:
    raise e

