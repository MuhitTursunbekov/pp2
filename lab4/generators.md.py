# Exercise 1
def printSquares(n):
    for x in range(n + 1):
        if x ** 2 < n:
            yield x ** 2
        else:
            break

myNums = printSquares(5)
for x in myNums:
    print(x)


# Exercise 2
def printEvenNums(n):
    for x in range(n):
        if x % 2 == 0:
            yield x

myNums = printEvenNums(11)
for x in myNums:
    print(x)


# Exercise 3
def generator(n):
    for x in range(n):
        if x % 3 == 0 and x % 4 == 0:
            yield x

myNums = generator(100)
for x in myNums:
    print(x)


# Exercise 4
def squares(a, b):
    for x in range(a, b + 1):
        yield x ** 2

myNums = squares(4, 11)
for x in myNums:
    print(x)


#exercise 5
def decrease(n):
    for x in range(n, -1, -1):
        yield x

myNums = decrease(100)
for x in myNums:
    print(x)
