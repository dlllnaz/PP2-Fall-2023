s = [{input() for j in range(int(input()))} for i in range(int(input()))]
a, b = set.intersection(*s), set.union(*s)
print(len(a), *sorted(a), sep='\n')
print(len(b), *sorted(b), sep='\n')
