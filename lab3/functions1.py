# exercise 1
def toOunces(grams):
    return 28.3495231 * grams

# exercise 2
def toCentigrade(F):
    return (5 / 9) * (F - 32)

# exercise 3
def solve(numheads, numlegs):
        x = (numlegs - 2 * numheads) / 2
        y = numheads - x
        return x, y

# exercise 4
def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if (n % i == 0):
            return False
        return True


def filter_prime(list):
    result = []
    for i in list:
        if (isPrime(i)):
            result.append(i)

    return result

# exercise 5
from itertools import permutations

def print_permutations():
    user_input = input("Введите строку: ")

    perms = permutations(user_input)

    for perm in perms:
        print(''.join(perm))

print_permutations()

# exercise 6
def reverse_input():
    user_input = input("Enter the string")
    return user_input[::-1]

# exercise 7
def has_33(nums):
    Has33 = False
    for i in range(len(nums) - 1):
        if (nums[i] == 3 and nums[i + 1] == 3):
            Has33 = True
    return Has33

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

# exercise 8
def spy_game(nums):
    count = 0

    for i in nums:
        if i == 0 and count == 0:
            count += 1
        elif i == 0 and count == 1:
            count += 1
        elif i == 7 and count == 2:
            return True
    return False

spy_game([1,2,4,0,0,7,5]) #--> True
spy_game([1,0,2,4,0,5,7]) #--> True
spy_game([1,7,2,0,4,5,0]) #--> False

# exercise 9
import math
pi = math.pi

def calculateVolumeOfSphere(R):
    return (4/3 * pi * R**3)

# exercise 10
def removeDuplicates(list):
    result = list(dict.fromkeys(list))
    return result

# exercise 11
def isPalindrome(s):
    return s == s[::-1]

# exercise 12
def histogram(nums):
    for num in nums:
        print('*' * num)

histogram([4, 9, 7])

# exercise 13
import random
def guessTheNumber():
    random_num = random.randint(1, 20)
    count = 0

    print('Hello! What is your name?')
    user_name = input()

    print(f'Well, {user_name}, I am thinking of a number between 1 and 20.')

    while True:
        print('Take a guess')
        user_input = int(input())
        count += 1

        if user_input < random_num:
            print('Your guess is too low.')
        elif user_input > random_num:
            print('Your guess is too high')
        else:
            print(f'Good job, {user_name}! You guessed my number in {count} guesses!')
            break

guessTheNumber()