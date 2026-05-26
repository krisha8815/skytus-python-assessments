# 1. Print name, age, and city in one line
name = "Krisha"
age = 20
city = "Surat"
print("1.", name, age, city)

# 2. Take user input for two numbers and print their sum
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
print("2. Sum =", a + b)

# 3. Convert Celsius to Fahrenheit
celsius = float(input("\nEnter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("3. Fahrenheit =", fahrenheit)

# 4. Store name in a variable and print it in uppercase
name = input("\nEnter your name: ")
print("4.", name.upper())

# 5. Calculate current age from birth year
birth_year = int(input("\nEnter your birth year: "))
current_age = 2026 - birth_year
print("5. Your age is", current_age)

# 6. Swap the values of two variables
a = input("\nEnter first value: ")
b = input("Enter second value: ")

print("Before swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

# 7. Calculate area of a rectangle
length = float(input("\nEnter length: "))
width = float(input("Enter width: "))
area = length * width
print("7. Area of rectangle =", area)

# 8. Check if a number is positive or negative
num = float(input("\nEnter a number: "))
if num >= 0:
    print("8. Positive Number")
else:
    print("8. Negative Number")

# 9. Print average of two numbers
a = float(input("\nEnter first number: "))
b = float(input("Enter second number: "))
average = (a + b) / 2
print("9. Average =", average)