n = int(input())
a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))
c = list(map(int, input().split(" ")))

count_dica = [0] * 10**5
count_dicc = [0] * 10**5
for i in range(n):
    count_dica[a[i]-1] += 1
    count_dicc[c[i]-1] += 1

count = 0
for i, bi in enumerate(b):
    count += count_dica[bi-1] * count_dicc[i]
print(count)
