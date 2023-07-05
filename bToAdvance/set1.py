#1
print("Hello, World!")

#2
# Integer
var_int = 10
print("Type of var_int:", type(var_int), "Value:", var_int)

# Float
var_float = 3.14
print("Type of var_float:", type(var_float), "Value:", var_float)

# String
var_string = "Hello, Python!"
print("Type of var_string:", type(var_string), "Value:", var_string)

# Boolean
var_bool = True
print("Type of var_bool:", type(var_bool), "Value:", var_bool)

# List
var_list = [1, 2, 3, 4, 5]
print("Type of var_list:", type(var_list), "Value:", var_list)

# Tuple
var_tuple = (6, 7, 8, 9, 10)
print("Type of var_tuple:", type(var_tuple), "Value:", var_tuple)

# Dictionary
var_dict = {"name": "John", "age": 25}
print("Type of var_dict:", type(var_dict), "Value:", var_dict)

# Set
var_set = {1, 2, 3, 4, 5}
print("Type of var_set:", type(var_set), "Value:", var_set)

#3
my_list = list(range(1, 11))
print("Original list:", my_list)

my_list.append(20)
print("After adding 20:", my_list)

my_list.remove(3)
print("After removing 3:", my_list)

my_list.sort()
print("After sorting:", my_list)

#4
numbers = [10, 20, 30, 40]
sum_of_numbers = sum(numbers)
average = sum_of_numbers / len(numbers)

print("Sum:", sum_of_numbers)
print("Average:", average)

#5
def reverse_string(input_string):
    return input_string[::-1]

string = "Python"
reversed_string = reverse_string(string)
print("Reversed string:", reversed_string)

#6
def count_vowels(input_string):
    vowels = "aeiou"
    count = 0
    for char in input_string.lower():
        if char in vowels:
            count += 1
    return count

string = "Hello"
vowel_count = count_vowels(string)
print("Number of vowels:", vowel_count)

#7
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

number = 13
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")

#8
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = 5
factorial_result = factorial(number)
print("Factorial of", number, "is", factorial_result)

#9
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

count = 5
fibonacci_sequence = fibonacci(count)
print(fibonacci_sequence)

#10
squared_numbers = [x**2 for x in range(1, 11)]
print(squared_numbers)

