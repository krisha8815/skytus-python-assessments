# 1. Handle division by zero error
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("1. Result:", num1 / num2)
except ZeroDivisionError:
    print("1. Error: Cannot divide by zero")


# 2. Handle invalid integer input
try:
    num = int(input("\nEnter an integer: "))
    print("2. You entered:", num)
except ValueError:
    print("2. Error: Invalid integer input")


# 3. Open a file and handle FileNotFoundError
try:
    with open("sample.txt", "r") as file:
        print("\n3. File Content:")
        print(file.read())
except FileNotFoundError:
    print("3. Error: File not found")


# 4. Demonstrate multiple exception blocks
try:
    num = int(input("\nEnter a number: "))
    result = 100 / num
    print("4. Result:", result)
except ValueError:
    print("4. Error: Invalid input")
except ZeroDivisionError:
    print("4. Error: Division by zero")


# 5. Use finally for resource cleanup
try:
    file = open("sample.txt", "r")
    print("\n5. File opened successfully")
except FileNotFoundError:
    print("5. File not found")
finally:
    try:
        file.close()
        print("5. File closed")
    except:
        pass


# 6. Custom exception for invalid age
class InvalidAgeError(Exception):
    pass

try:
    age = int(input("\nEnter age: "))
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
    print("6. Age is valid")
except InvalidAgeError as e:
    print("6. Error:", e)


# 7. Handle IndexError when accessing a list
try:
    numbers = [10, 20, 30]
    index = int(input("\nEnter index: "))
    print("7. Value:", numbers[index])
except IndexError:
    print("7. Error: Index out of range")


# 8. Take two numbers and handle all possible errors
try:
    a = float(input("\nEnter first number: "))
    b = float(input("Enter second number: "))
    print("8. Division Result:", a / b)
except ValueError:
    print("8. Error: Invalid number")
except ZeroDivisionError:
    print("8. Error: Cannot divide by zero")
except Exception as e:
    print("8. Unexpected Error:", e)


# 9. Log errors to a file
try:
    num = int(input("\nEnter a number: "))
    result = 100 / num
    print("9. Result:", result)
except Exception as e:
    with open("error_log.txt", "a") as log:
        log.write(str(e) + "\n")
    print("9. Error logged to error_log.txt")


# 10. Validate email format
try:
    email = input("\nEnter email: ")

    if "@" not in email or "." not in email:
        raise ValueError("Invalid Email Format")

    print("10. Valid Email")
except ValueError as e:
    print("10. Error:", e)