#problem1
people = [("John", 25), ("Jane", 30)]

for name, age in people:
    print(f"{name} is {age} years old.")



#problem2
ages = {"John": 25, "Jane": 30}

# Add a new name-age pair
ages.update({"Tom": 40})

# Update the age of a name
ages["John"] = 26

# Delete a name
del ages["John"]

print(ages)



#problem3
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return None

nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)
print(result)


#problem4
def is_palindrome(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False

word = "madam"

if is_palindrome(word):
    print(f"The word {word} is a palindrome.")
else:
    print(f"The word {word} is not a palindrome.")



#problem5
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print(sorted_arr)



#problem6
from queue import LifoQueue

stack = LifoQueue()

# Push elements onto the stack
stack.put(1)
stack.put(2)

# Pop elements from the stack
print(stack.get())  # Output: 2
print(stack.get())  # Output: 1




#problem7
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)



#problem8

# def count_words(input_file, output_file):
#     with open(input_file, 'r') as file:
#         content = file.read()
#         word_count = len(content.split())

#     with open(output_file, 'w') as file:
#         file.write(f"Number of words: {word_count}")

# count_words("input.txt", "output.txt")


#problem9
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None

num1 = 5
num2 = 0

division_result = divide_numbers(num1, num2)
print(division_result)


