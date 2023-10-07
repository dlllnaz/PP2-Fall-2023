N, K = [int(s) for s in input().split()]
work_d = set([day for day in range(1, N + 1) if day % 7 not in (6, 0)])
no_s = set(work_d)
for party in range(K):
    a, b = [int(s) for s in input().split()]
    max_strikes = (N - a) // b + 1
    no_s -= { a + b*i for i in range(max_strikes)}
print(len(work_d) - len(no_s))
