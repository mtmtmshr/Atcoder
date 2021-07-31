_ = input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))

min_ab = 10 ** 9
for i in a:
    for j in b:
        if abs(i-j) < min_ab:
            min_ab = abs(i-j)

print(min_ab)
