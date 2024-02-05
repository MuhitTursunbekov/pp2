# exercise 1
class toUpper:
  def __init__(self):
    self.user_input = ''

  def getString(self):
    self.user_input = input("Enter the string: ")

  def printString(self):
    print(self.user_input.upper())

s = toUpper()
s.getString()
s.printString()


# exercise 2
class Shape:
    def area(self):
        print('Area is 0')


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(self.length ** 2)

shape = Shape()
shape.area()

square = Square(5)
square.area()


# exercise 3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
      print(self.length * self.width)

rectangle = Rectangle(5, 6)
rectangle.area()


# exercise 4
class Point:
    def getCoordinates(self, x1, y1):
        self.x1 = x1
        self.y1 = y1

    def showCoordinates(self):
        print(f'Coordinates: {self.x1}, {self.y1} ')

    def moveCoordinates(self, x2, y2):
        self.x2 = x2
        self.y2 = y2

    def distBetweenCoordinates(self):
        print(((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2) ** 0.5)

point = Point()
point.getCoordinates(1, 2)
point.moveCoordinates(5, 6)
point.distBetweenCoordinates()


# exercise 5
class Account:
  def __init__(self):
        self.user_balance = 2156

  def owner(self):
    self.user_name = input('What is your name? ')

  def balance(self):
    print(f'You have {self.user_balance}$ in your balance')

  def withdraw(self):
    self.user_withdraw = int(input('How much money you want to withdraw? '))
    if (self.user_withdraw > self.user_balance):
        print('Not enough money to withdraw')
    else:
        self.user_balance -= self.user_withdraw
        print(f'You withdrew {self.user_withdraw}$ succesfully!')

  def deposit(self):
    deposit_interest_rate = 5
    self.user_deposit = int(input('How much money do you want to deposit? '))
    self.user_balance += (self.user_deposit + (deposit_interest_rate * self.user_deposit) / 100)

person = Account()

person.owner()

person.balance()

person.withdraw()

person.balance()

person.deposit()

person.balance()