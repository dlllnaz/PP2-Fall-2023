a = int(input())
b = int(input())
c = int(input())
d = int(input())

first=0
second=0
if(a%2==0 and b%2==0):
    first=1
elif(a%2==1 and b%2==1):
    first=1
else:
    first=0

if(c%2==0 and d%2==0):
    second=1
elif(c%2==1 and d%2==1):
    second=1
else:
    second=0
    
if(first==second):
    print("YES")
else:
    print("NO")
