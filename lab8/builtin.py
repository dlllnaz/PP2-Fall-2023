#1
from functools import reduce
from operator import mul
def multiply_n(numbers):
    result = reduce(mul, numbers, 1)
    return result
number_list = [2, 3, 4, 5]
result = multiply_n(number_list)
print(f"The product is: {result}")
#2
def count_u_l(input_str):
    upper_c = sum(1 for char in input_str if char.isupper())
    lower_c = sum(1 for char in input_str if char.islower())
    return upper_c, lower_c
input_string = "Hello, World!"
upper, lower = count_u_l(input_string)
print(f"Original String: {input_string}")
print(f"Number of Upper Case Letters: {upper}")
print(f"Number of Lower Case Letters: {lower}")
#3
def is_palindrome(input_str):
    cleaned_str = input_str.lower()
    cleaned_str = cleaned_str.replace(" ", "")
    return cleaned_str == cleaned_str[::-1]
user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
#4
import time
import math
def delayed_square(number, delay_ms):
    time.sleep(delay_ms / 1000)
    result = math.sqrt(number)
    return result
number = 25100
delay = 2123
result = delayed_square(number, delay)
print(f"Square root of {number} after {delay} milliseconds is {result}")
#5
def all_true_elements(tuple_data):
    return all(tuple_data)
my_tuple1 = (True, True, True)
result1 = all_true_elements(my_tuple1)
print(result1) 


