import os
import random
import datetime
import math

with open("my_math.py", "w") as f:
    f.write("""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
""")

import my_math

print("===== CUSTOM MATH MODULE =====")
print("Addition:", my_math.add(10, 5))
print("Subtraction:", my_math.subtract(10, 5))
print("Multiplication:", my_math.multiply(10, 5))
print("Division:", my_math.divide(10, 5))

with open("string_ops.py", "w") as f:
    f.write("""
def to_upper(text):
    return text.upper()

def to_lower(text):
    return text.lower()

def reverse(text):
    return text[::-1]
""")

import string_ops

print("\n===== STRING OPERATIONS MODULE =====")
text = "Hello Python"
print("Upper:", string_ops.to_upper(text))
print("Lower:", string_ops.to_lower(text))
print("Reverse:", string_ops.reverse(text))

print("\n===== RANDOM INTEGERS =====")
for i in range(5):
    print(random.randint(1, 100))

print("\n===== CURRENT DATE AND TIME =====")
now = datetime.datetime.now()
print(now)

print("\n===== FACTORIAL =====")
num = 5
print(f"Factorial of {num} =", math.factorial(num))

os.makedirs("shapes", exist_ok=True)

with open("shapes/__init__.py", "w") as f:
    pass

with open("shapes/circle.py", "w") as f:
    f.write("""
import math

def area(radius):
    return math.pi * radius * radius
""")

with open("shapes/rectangle.py", "w") as f:
    f.write("""
def area(length, width):
    return length * width
""")

from shapes.circle import area as circle_area
from shapes.rectangle import area as rectangle_area

print("\n===== SHAPES PACKAGE =====")
print("Circle Area:", round(circle_area(5), 2))
print("Rectangle Area:", rectangle_area(4, 6))

from my_math import add, subtract, multiply

print("\n===== MULTIPLE FUNCTION IMPORT =====")
print("Add:", add(20, 10))
print("Subtract:", subtract(20, 10))
print("Multiply:", multiply(20, 10))

print("\n===== SHUFFLE LIST =====")
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

print("\n===== DATE DIFFERENCE =====")

date1 = datetime.date(2025, 1, 1)
date2 = datetime.date(2025, 12, 31)

difference = date2 - date1
print("Difference in days:", difference.days)

print("\n===== FILES IN CURRENT DIRECTORY =====")
for file in os.listdir("."):
    print(file)

print("\nProgram Completed Successfully!")