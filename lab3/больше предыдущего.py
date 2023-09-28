elements = input().split()
elements = [int(element) for element in elements]
for i in range(1, len(elements)):
    if elements[i] > elements[i - 1]:
        print(elements[i], end=' ')