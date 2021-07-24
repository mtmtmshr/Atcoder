R, X, Y = list(map(int, input().split(" ")))


distance = (X**2 + Y**2) ** 0.5
count = 0
while distance >= 2 * R:
    count += 1
    distance -= R

if R - distance == 0:
    count += 1
else:
    count += 2
print(count)
