n=int(input())
m=int(input())
x=int(input())
y=int(input())
if(m<n):
    n,m=m,n
xmin=min(x,n-x)
ymin=min(y,m-y)
print(min(xmin,ymin))