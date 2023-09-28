A = [int(x) for x in input().split()]
for element in A:
    if element % 2 == 0:
        print(element, end=' ')