_ = input()
str1 = input()
t = ""
for i in range(len(str1)):
    t += str1[i]
    if len(t) >= 3 and t[-3:] == "fox":
        t = t[:-3:]
print(len(t))
