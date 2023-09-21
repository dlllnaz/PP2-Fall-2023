a = int(input())
b = int(input())
c = int(input())
if (a > c) and (b > c):
    print(c)
elif (c > b) and (a > b):
    print (b)
else:
    print(a)