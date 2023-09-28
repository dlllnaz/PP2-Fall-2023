elements = input().split()
elements = [int(element) for element in elements]

for i in range(0, len(elements), 2):
    print(elements[i])