import sys
_ = input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))

min_ab = 10 ** 9
a.sort()
b.sort()
len_a = len(a)
len_b = len(b)
i = 0
j = 0
result = sys.maxsize
while ( i < len_a and j < len_b):
    a_b = abs(a[i]-b[j])
    if a_b < result:
        result = a_b

    if a[i] < b[j]:
        i += 1
    else:
        j += 1

print(result)