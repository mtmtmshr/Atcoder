import math


if __name__ == "__main__":
    s, p = list(map(int, input().split(" ")))
    f = True
    for i in range(1, int(math.sqrt(p))+1):
        if p % i != 0:
            continue
        else:
            if s == i + int(p/i):
                print("Yes")
                f = False
                break
    if f:
        print("No")
