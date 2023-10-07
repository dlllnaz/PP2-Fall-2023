A = {i+1 for i in range(int(input()))}
while True:
    question = input()
    if question == 'HELP': break
    B = {int(i) for i in question.split()}
    if len(A - B) >= len(A & B):
        print('NO')
        A -= B
    else:
        print('YES')
        A &= B
print(*sorted(A))
