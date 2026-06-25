# Conditional Statements

age = int(input("Please enter your age: "))

if age >= 18:
    print("Hey you are an adult.")
else:
    print("You are a minor.")


marks = int(input("Enter Marks: "))

if marks >= 90 and marks <=100:
    print("Grade A")
elif marks >= 70 and marks < 90:
    print("Grade B")
elif marks >= 50 and marks < 70:
    print("Grade C")
elif marks >= 0 and marks < 50:
    print("Fail")
else:
    print("Please enter marks between 0 - 100")


num = int(input("Enter Number: "))

if num%2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")
