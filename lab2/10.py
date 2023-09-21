a=int(input())
b=int(input())
c=int(input())
d=int(input())
if(a==c and (b>d or b<d)):
    print("YES")
elif(b==d and (a>c or a<c)):
    print("YES")
elif(a+b==c+d or a-b==c-d):
    print("YES")
else:
    print("NO")
