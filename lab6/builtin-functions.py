#exercise 1
import math

def multiply_list(numbers):
    result = math.prod(numbers)
    return result


#exercise 2
def count_case(string):
    uppercase_count = sum(1 for char in string if char.isupper())
    lowercase_count = sum(1 for char in string if char.islower())
    return uppercase_count, lowercase_count


#exercise 3
def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string


#exercise 4
import time
import math

def square_root_after_delay(number, milliseconds):
    time.sleep(milliseconds / 1000)  # Convert milliseconds to seconds
    result = math.sqrt(number)
    return result


#exercise 5
def all_true_elements(tup):
    return all(tup)
