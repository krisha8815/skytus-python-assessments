# 1. Animal -> Dog, Cat
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


print("===== 1. ANIMAL HIERARCHY =====")
dog = Dog()
cat = Cat()
dog.sound()
cat.sound()

# 2. Vehicle -> Car -> ElectricCar
class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


class ElectricCar(Car):
    def charge(self):
        print("Electric Car is charging")


print("\n===== 2. VEHICLE HIERARCHY =====")
tesla = ElectricCar()
tesla.start()
tesla.drive()
tesla.charge()

# 3. Method Overriding
class Parent:
    def show(self):
        print("Parent Class Method")


class Child(Parent):
    def show(self):
        print("Child Class Overridden Method")


print("\n===== 3. METHOD OVERRIDING =====")
obj = Child()
obj.show()

# 4. Multiple Inheritance
class Father:
    def skill1(self):
        print("Driving")


class Mother:
    def skill2(self):
        print("Cooking")


class Child(Father, Mother):
    pass


print("\n===== 4. MULTIPLE INHERITANCE =====")
c = Child()
c.skill1()
c.skill2()

# 5. Polymorphism with Shapes
class Circle:
    def area(self):
        return 3.14 * 5 * 5


class Rectangle:
    def area(self):
        return 4 * 6


def print_area(shape):
    print("Area =", shape.area())


print("\n===== 5. POLYMORPHISM =====")
print_area(Circle())
print_area(Rectangle())

# 6. Bank System
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def display_balance(self):
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    pass


class CurrentAccount(BankAccount):
    pass


print("\n===== 6. BANK SYSTEM =====")
savings = SavingsAccount(5000)
current = CurrentAccount(10000)

savings.display_balance()
current.display_balance()

# 7. Private Attributes with Getter/Setter
class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name


print("\n===== 7. ENCAPSULATION =====")
p = Person("John")
print("Name:", p.get_name())

p.set_name("Alice")
print("Updated Name:", p.get_name())

# 8. Teacher and Student Inheritance
class Teacher:
    def teach(self):
        print("Teacher is teaching")


class Student(Teacher):
    def study(self):
        print("Student is studying")


print("\n===== 8. TEACHER-STUDENT =====")
s = Student()
s.teach()
s.study()

# 9. MusicPlayer -> Spotify
class MusicPlayer:
    def play(self):
        print("Playing music...")


class Spotify(MusicPlayer):
    def play(self):
        print("Playing music from Spotify...")


print("\n===== 9. MUSIC PLAYER =====")
sp = Spotify()
sp.play()

# 10. Use of super()
class Employee:
    def __init__(self, name):
        self.name = name
        print("Employee Constructor Called")


class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Department:", self.department)


print("\n===== 10. SUPER() DEMONSTRATION =====")
m = Manager("Parth", "IT")
m.display()

print("\nAll OOP Programs Executed Successfully!")