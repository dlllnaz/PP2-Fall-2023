#Create a generator that generates the squares of numbers up to some number N
#task1
def generate_s(N):
    for i in range(1, N + 1):
        yield i ** 2
N = int(input())
squares = generate_s(N)
for square in squares:
    print(square)
#task2
def even_numbers_generator(n):
    for i in range(0, n + 1, 2):
        yield i
def main():
    try:
        n = int(input())
        even_numbers = even_numbers_generator(n)
        result = ', '.join(map(str, even_numbers))
        print("Even numbers are: {}".format(n, result))
    except ValueError:
        print()
if _name_ == "_main_":
    main()
#task3
def div_by(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input())  
for num in div_by(n):
    print(num)
    
#task4
def squares(a, b):
    for num in range(a, b + 1):
        yield num * num
a = 8
b = 9
for square in squares(a, b):
    print(square)
#task5
def count_down(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input())
for num in count_down(n):
    print(num)