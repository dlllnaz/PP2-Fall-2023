import math
#TASK1
class StringManipulator:
    def _init_(self):
        self.string = ""
    def get_string(self):
        self.string = input()
    def print_string_uppercase(self):
        print(self.string.upper())
manipulator = StringManipulator()
manipulator.get_string()
manipulator.print_string_uppercase()

#TASK2
class Shape:
    def Area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def Area(self):
        self.area = self.length*self.length
        return self.area
shape = Shape()
print(shape.Area())
length = float(input())
square = Square(length)
print(square.Area())

#TASK3
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        area_of_rectangle = self.length * self.width
        print(f" {area_of_rectangle}")
rectangle = Rectangle(4, 6)
rectangle.area()

#TASK4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x, self.y)

    def move(self,new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, point2):
        dx = self.x-point2.x
        dy = self.y-point2.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance
    
x1=int(input())
y1=int(input())

x2=int(input())
y2=int(input())

point1 = Point(x1, y1)
point2 = Point(x2, y2)

point1.show()

x3=int(input())
y3=int(input())

point1.move(x3, y3)
point1.show()

distance = point1.dist(point2)
print(distance)

#TASK5
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} units. New balance: {self.balance} units")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount} units. New balance: {self.balance} units")
        else:
            print("Insufficient funds. Withdrawal denied.")

account = BankAccount("John Doe", 1000)
print("Account owner:", account.owner)
print("Initial balance:", account.balance)
account.deposit(500)
account.withdraw(200)
account.withdraw(800)

#TASK6
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
numbers = [int(s) for s in input().split()]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Original list:", numbers)
print("Prime numbers:", prime_numbers)
