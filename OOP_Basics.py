# 1. Car Class
class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self, increase):
        self.speed += increase
        print(f"Accelerated. Current Speed: {self.speed} km/h")

    def brake(self, decrease):
        self.speed -= decrease
        if self.speed < 0:
            self.speed = 0
        print(f"Braked. Current Speed: {self.speed} km/h")


print("===== 1. CAR CLASS =====")
car = Car("Toyota", "Camry")
car.accelerate(50)
car.brake(20)

# 2. BankAccount Class
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Balance:", self.balance)


print("\n===== 2. BANK ACCOUNT =====")
acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
acc.show_balance()

# 3. Student Class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)


print("\n===== 3. STUDENT CLASS =====")
student = Student("John", [80, 90, 85, 95])
print("Average Marks:", student.average())

# 4. Rectangle Class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


print("\n===== 4. RECTANGLE CLASS =====")
rect = Rectangle(10, 5)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())

# 5. Employee Class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee:", self.name)
        print("Salary:", self.salary)


print("\n===== 5. EMPLOYEE CLASS =====")
emp = Employee("Alice", 50000)
emp.display()

# 6. Book Class
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title :", self.title)
        print("Author:", self.author)
        print("Price :", self.price)


print("\n===== 6. BOOK CLASS =====")
book = Book("Python Basics", "John Smith", 499)
book.display()

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius


print("\n===== 7. CIRCLE CLASS =====")
circle = Circle(7)
print("Area:", round(circle.area(), 2))
print("Circumference:", round(circle.circumference(), 2))

# 8. Laptop Class
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def apply_discount(self, percentage):
        discount = self.price * percentage / 100
        self.price -= discount
        print("Discounted Price:", self.price)


print("\n===== 8. LAPTOP CLASS =====")
laptop = Laptop("Dell", 80000)
laptop.apply_discount(10)

# 9. Flight Class
class Flight:
    def __init__(self, flight_no, seats):
        self.flight_no = flight_no
        self.available_seats = seats

    def book_seat(self, count):
        if count <= self.available_seats:
            self.available_seats -= count
            print(f"{count} seat(s) booked.")
        else:
            print("Not enough seats available.")

    def show_seats(self):
        print("Available Seats:", self.available_seats)


print("\n===== 9. FLIGHT CLASS =====")
flight = Flight("AI101", 100)
flight.book_seat(5)
flight.show_seats()

# 10. Shop Class
class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        print("Products in Shop:")
        for product in self.products:
            print("-", product)


print("\n===== 10. SHOP CLASS =====")
shop = Shop()
shop.add_product("Laptop")
shop.add_product("Mobile")
shop.add_product("Headphones")
shop.list_products()

print("\nAll Class Programs Executed Successfully!")