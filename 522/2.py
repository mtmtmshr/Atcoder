a = input()
for s in a[::-1]:
    if s == "6":
        print(9, end="")
    elif s == "9":
        print(6, end="")
    else:
        print(s, end="")
print("")
