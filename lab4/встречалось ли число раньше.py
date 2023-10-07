def check_d(sequence):
    seen_n = set()
    for number in sequence:
        if number in seen_n:
            print("YES")
        else:
            print("NO")
            seen_n.add(number)
numbers_s = input().split()
numbers_s = [int(num) for num in numbers_s]
check_d(numbers_s)