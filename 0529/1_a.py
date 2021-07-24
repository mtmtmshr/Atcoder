import itertools
n = int(input())

max1x = -10 ** 9 - 1
max2x = -10 ** 9 - 1
min1x = 10 ** 9 + 1
min2x = 10 ** 9 + 1
max1y = -10 ** 9 - 1
max2y = -10 ** 9 - 1
min1y = 10 ** 9 + 1
min2y = 10 ** 9 + 1

for _ in range(n):
    x, y = list(map(int, input().split()))
    if x > max1x:
        max2x = max1x
        max1x = x
    elif x > max2x:
        max2x = x
    if x < min1x:
        min2x = min1x
        min1x = x
    elif x < min2x:
        min2x = x
    if y > max1y:
        max2y = max1y
        max1y = y
    elif y > max2y:
        max2y = y
    if y < min1y:
        min2y = min1y
        min1y = y
    elif y < min2y:
        min2y = y


if max1x - min1x == max1y - min1y:
    print(max1x - min1x)
else:
    xflag = True
    if max1x - min1x > max1y - min1y:
        max1 = max1x - min1x
    else:
        max1 = max1y - min1y
        xflag = False

    sa1 = max1x - max2x
    sa2 = min2x - min1x
    sa3 = max1y - max2y
    sa4 = min2y - min1y

    if xflag:
        if sa1 > sa2:
            kouho = max1 - sa2
        else:
            kouho = max1 - sa1
        if kouho < max1y - min1y:
            max2 = max1y - min1y
        else:
            max2 = kouho
    else:
        if sa3 > sa4:
            kouho = max1 - sa4
        else:
            kouho = max1 - sa3
        if kouho < max1x - min1x:
            max2 = max1x - min1x
        else:
            max2 = kouho

    print(max2)
