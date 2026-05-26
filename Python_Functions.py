# 1. Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
print("1. Prime:", is_prime(num))


# 2. Function to reverse a string
def reverse_string(text):
    return text[::-1]

text = input("\nEnter a string: ")
print("2. Reversed String:", reverse_string(text))


# 3. Function to find factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("\nEnter a number: "))
print("3. Factorial:", factorial(num))


# 4. Function to calculate simple interest
def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(input("\nEnter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))
print("4. Simple Interest:", simple_interest(p, r, t))


# 5. Function to check if a word is palindrome
def is_palindrome(word):
    return word == word[::-1]

word = input("\nEnter a word: ")
print("5. Palindrome:", is_palindrome(word))


# 6. Function to count vowels in a string
def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            count += 1
    return count

text = input("\nEnter a string: ")
print("6. Number of Vowels:", count_vowels(text))


# 7. Function to merge two lists
def merge_lists(list1, list2):
    return list1 + list2

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("7. Merged List:", merge_lists(list1, list2))


# 8. Function to find GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
print("8. GCD:", gcd(a, b))


# 9. Function to find area of rectangle
def area_rectangle(length, width):
    return length * width

length = float(input("\nEnter length: "))
width = float(input("Enter width: "))
print("9. Area of Rectangle:", area_rectangle(length, width))


# 10. Function to check Armstrong number
def is_armstrong(num):
    digits = len(str(num))
    total = sum(int(digit) ** digits for digit in str(num))
    return total == num

num = int(input("\nEnter a number: "))
print("10. Armstrong Number:", is_armstrong(num))