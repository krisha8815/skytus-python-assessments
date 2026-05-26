# 1. Check if a person is eligible to vote
age = int(input("Enter your age: "))
if age >= 18:
    print("1. Eligible to vote")
else:
    print("1. Not eligible to vote")

# 2. Grade calculator
marks = float(input("\nEnter marks: "))
if marks >= 90:
    print("2. Grade A")
elif marks >= 80:
    print("2. Grade B")
else:
    print("2. Grade C")

# 3. Traffic light simulation
color = input("\nEnter traffic light color (Red/Yellow/Green): ").lower()
if color == "red":
    print("3. Stop")
elif color == "yellow":
    print("3. Wait")
elif color == "green":
    print("3. Go")
else:
    print("3. Invalid color")

# 4. ATM withdrawal check
balance = float(input("\nEnter account balance: "))
withdraw = float(input("Enter withdrawal amount: "))
if withdraw <= balance:
    print("4. Withdrawal successful")
else:
    print("4. Insufficient balance")

# 5. Check if a number is positive, negative, or zero
num = float(input("\nEnter a number: "))
if num > 0:
    print("5. Positive")
elif num < 0:
    print("5. Negative")
else:
    print("5. Zero")

# 6. Check if a number lies within a given range
num = int(input("\nEnter a number: "))
start = int(input("Enter range start: "))
end = int(input("Enter range end: "))
if start <= num <= end:
    print("6. Number is within the range")
else:
    print("6. Number is outside the range")

# 7. Username & password verification
username = input("\nEnter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("7. Login successful")
else:
    print("7. Invalid username or password")

# 8. Electricity bill calculator
units = float(input("\nEnter units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
else:
    bill = units * 10

print("8. Electricity Bill =", bill)

# 9. Simple calculator
num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("9. Result =", num1 + num2)
elif operator == "-":
    print("9. Result =", num1 - num2)
elif operator == "*":
    print("9. Result =", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("9. Result =", num1 / num2)
    else:
        print("9. Cannot divide by zero")
else:
    print("9. Invalid operator")

# 10. Check type of triangle
a = float(input("\nEnter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if a == b == c:
    print("10. Equilateral Triangle")
elif a == b or b == c or a == c:
    print("10. Isosceles Triangle")
else:
    print("10. Scalene Triangle")