# 1. Calculate the remainder of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("1. Remainder:", a % b)

# 2. Check if a number is even or odd
num = int(input("\nEnter a number: "))
if num % 2 == 0:
    print("2. Even")
else:
    print("2. Odd")

# 3. Compare two numbers and print the larger one
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("3. Larger number:", a)
else:
    print("3. Larger number:", b)

# 4. Calculate the square and cube of a number
num = int(input("\nEnter a number: "))
print("4. Square:", num ** 2)
print("4. Cube:", num ** 3)

# 5. Check if two entered numbers are equal
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
if a == b:
    print("5. Numbers are equal")
else:
    print("5. Numbers are not equal")

# 6. Print True if both numbers are positive, else False
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
print("6.", a > 0 and b > 0)

# 7. Convert float to integer
num = float(input("\nEnter a float number: "))
print("7. Integer value:", int(num))

# 8. Take a number as string, convert to int, and multiply by 10
num = input("\nEnter a number: ")
print("8. Result:", int(num) * 10)

# 9. Use and & or operators to check multiple conditions
age = int(input("\nEnter age: "))
salary = int(input("Enter salary: "))
print("9. Using AND:", age >= 18 and salary >= 20000)
print("9. Using OR:", age >= 18 or salary >= 20000)

# 10. Divide two numbers and print quotient and remainder
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
print("10. Quotient:", a // b)
print("10. Remainder:", a % b)