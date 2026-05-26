# 1. Print numbers from 1 to 10
print("1. Numbers from 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print()

# 2. Display multiplication table for a given number
num = int(input("\nEnter a number for multiplication table: "))
print("2. Multiplication Table:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 3. Find factorial of a number
num = int(input("\nEnter a number to find factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("3. Factorial =", factorial)

# 4. Generate the first N Fibonacci numbers
n = int(input("\nEnter N for Fibonacci series: "))
a, b = 0, 1
print("4. Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# 5. Check if a number is prime
num = int(input("\nEnter a number to check prime: "))
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("5. Prime Number")
else:
    print("5. Not a Prime Number")

# 6. Reverse a number
num = int(input("\nEnter a number to reverse: "))
reverse = 0
temp = num

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

print("6. Reversed Number =", reverse)

# 7. Count digits in a number
num = input("\nEnter a number: ")
print("7. Number of Digits =", len(num))

# 8. Find sum of even numbers between 1 and 100
sum_even = 0
for i in range(2, 101, 2):
    sum_even += i
print("8. Sum of Even Numbers =", sum_even)

# 9. Print a pyramid pattern
rows = int(input("\nEnter number of rows for pyramid: "))
print("9. Pyramid Pattern:")
for i in range(1, rows + 1):
    print("*" * i)

# 10. Find all divisors of a number
num = int(input("\nEnter a number: "))
print("10. Divisors:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
print()