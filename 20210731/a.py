a, b = list(map(int, input().split()))

if a > 0:
    if b == 0:
        print("Gold")
    else:
        print("Alloy")
elif a == 0:
    if b > 0:
        print("Silver")