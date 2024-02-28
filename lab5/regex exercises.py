# Exercise 1
import re

def match_string(text):
    pattern = r'ab*'
    if re.search(pattern, text):
        return True
    return False

# Test
test_strings = ["a", "ab", "abb", "abbb", "ac", "b", "bb"]
for test_string in test_strings:
    if match_string(test_string):
        print('pattern matches')
    else:
        print('pattern does not match')


# Exercise 2
import re

def pattern_match(string):
    pattern = r'abbb*' # or we can be rewrite like r'ab{2,3}'
    if re.search(pattern, string):
        return True
    return False

test_strings = ["abb", "abbb", "abbbb", "aabbb", "ab", "abbcc", "ac", "bb", "b"]

for test_string in test_strings:
    if pattern_match(test_string):
        print('pattern match')
    else:
        print('pattern does not much')


# Exercise 3
import re

def find_sequence(string):
    pattern = r'\b[a-z]+_[a-z]+\b'
    sequences = re.search(pattern, string)
    return sequences if sequences else []


    # Функция для тестирования
tests = [
    "abc_def_ghi", "abc_def", "def_ghi",
    "hello_world_python_is_cool", "hello_world", "world_python", "python_is", "is_cool",
    "No_sequences_here", ""
]
for test in tests:
    if find_sequence(test):
        print('Seqeunce found')
    else:
        print('Sequence not found')


# Exercise 4
import re

def find_sequence(s):
    pattern = r'[A-Z]+[a-z]'
    sequences = re.findall(pattern, s)
    return sequences if sequences else []

tests = [
    "AbcDefGhi", "abcDef", "DefGhi", "HelloWorldPythonIsCool", "helloWorld", "WorldPython", "PythonIs", "IsCool",
    "NoSequencesHere", "", "Multiple   WordsHere"
        ]

for test in tests:
    if find_sequence(test):
        print('Sequence found')
    else:
        print('Sequence not found')


# Exercise 5
import re

def find_sequence(s):
    pattern = r'a.b' # a.b$
    sequences = re.search(pattern, s)
    return sequences if sequences else []

strings = [
    "abc", "axb", "aaaab", "a$b", "a\nb",
    "abb", "a", "bcd", "ab",
    "asjkdabcaksjdk", "asdjfabcaksdfj", "adkfjabc",
    "aAbB", "aXb", "aaaabb", "a$bC", "a\nB",
    "aBB", "AB", "BCD", "AB"
]

for string in strings:
    if find_sequence(string):
        print('Sequence found')
    else:
        print('Sequence not found')


# Exercise 6
import re

def replace(s):
    pattern = r'[ ,.]'
    replaced_s = re.sub(pattern, ':', s)
    return replaced_s

tests = [
    "This is a test string.", "This:is:a:test:string:",
    "Hello, world!", "Hello::world:",
    "One, two, three.", "One::two::three:",
    "",  # Пустая строка
    "NoReplacementNeeded", "NoReplacementNeeded",  # Строка без символов, требующих замены
    "Spaces   and   multiple, commas. And... dots", "Spaces:::and:::multiple:::commas:::And:::d:::ots"  # Множественные пробелы и знаки препинания
]

for test in tests:
    print(replace(test))


# Exercise 7
import re

def snake_to_camel(snake_case_str):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), snake_case_str)

snake_case_input = input("Enter a string in snake_case: ")
camel_case_output = snake_to_camel(snake_case_input)
print(camel_case_output)


# Exercise 8
import re

def split(s):
    return re.findall(r'[A-Z][a-z]*', s)

user_input = input("input a string in c camel case: ")
words = split(user_input)
print(words) # or we can loop it


# Exercise 9
import re

def insert(camel_case_str):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', camel_case_str)

camel_case_input = input("input a string in camel case ")
spaced_output = insert(camel_case_input)
print(spaced_output)


# Exercise 10 
import re

def camel_to_snake(camel_case_str):
    snake_case_str = re.sub('([a-z0-9])([A-Z])', r'\1_\2', camel_case_str)
    return snake_case_str.lower()

input_str = input("Enter a camel case string: ")
snake_case_output = camel_to_snake(input_str)
print("Converted snake case string:", snake_case_output)