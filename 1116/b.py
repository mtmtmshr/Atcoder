sx, sy, gx, gy = list(map(int, input().split(" ")))

a = (-gy-sy)/float(gx-sx)
b = sy - a * sx
print(float(-b)/a)
