#task1
def ounces_to_grams(ounces):
    grams= ounces/28.3495231
    return grams
ounces = int(input())
grams = ounces_to_grams(ounces)
print(f"{ounces} ounces is equal to {grams:.2f} grams")

#task2
def far_to_cel(far):
    centigrade = (5 / 9) * (far - 32)
    return centigrade
far = int(input())
centigrade = far_to_cel(far)
print(f"{far} farenheit temp. is equal to {centigrade:.2f} centigrade temperature")

#task3
def solve(numheads, numlegs):
    y = (numlegs - 2 * numheads) / 2
    x = numheads - y
    if x < 0 or y < 0 or x != int(x) or y != int(y):
        return "No valid solution found."
    return int(x), int(y)
numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
print(result)

#task4
import math
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = math.isqrt(n) + 1
    for i in range(3, max_divisor, 2):
        if n % i == 0:
            return False
    return True
def filter_prime(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers
numbers_list = [int(s) for s in input().split()]
prime_numbers_list = filter_prime(numbers_list)
print("Prime numbers", prime_numbers_list)

#task5
from itertools import permutations
def print_permutations(input_string):
    perm_list = permutations(input_string)
    for perm in perm_list:
        print(''.join(perm))
user_input = input()
print_permutations(user_input)

#task6
def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words
user_input = input()
reversed_words = reverse_sentence(user_input)
print(reversed_words)

#task7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
print(has_33([int(s) for s in input().split()]))   

#task8
def spy_game(nums):
    count_0 = 0
    count_7 = 0
    for num in nums:
        if num == 0 and count_7 == 0:
            count_0 += 1
        elif num == 0 and count_7 == 1:
            count_0 += 1
        elif num == 7 and count_0 == 2:
            count_7 += 1
    return count_0 == 2 and count_7 == 1
print(spy_game([int(s) for s in input().split()]))  

#task9
def volume_of_sphere(radius):
    volume= (4/3)* 3.14 * (radius^3)
    return volume
radius = int(input())
volume = volume_of_sphere(radius)
print(f"{volume:.2f}")

#task10
def unique_el(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list
print(unique_el([int(s) for s in input().split()]))  
       
#task11
def palindrome(string):
    s = string[::-1]
    if(string == s):
        print('True')
    else:
        print('False')

string = str(input())
palindrome(string)

#task12
def histogram(numbers):
    for num in numbers:
        print('*' * num)
histogram([int(s) for s in input().split()]

#task13
import random
def guess_the_number():
    secret_number = random.randint(1, 20)
    print("Hello! What is your name?")
    user_name = input()
    print(f"Well, {user_name}, I am thinking of a number between 1 and 20.")
    num_guesses = 0
    while True:
        print("Take a guess.")
        user_guess = int(input())
        num_guesses += 1
        if user_guess < secret_number:
            print("Your guess is too low.")
        elif user_guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {user_name}! You guessed my number in {num_guesses} guesses!")
            break
guess_the_number()
          
