n = input()
sum = 0
for s in n[::1]:
    sum += int(s)
 
if sum % 9 == 0:
    print("Yes")
else:
    print("No")

