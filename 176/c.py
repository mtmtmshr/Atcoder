n = int(input())
members = list(map(int, input().split(" ")))
 
 
sum = 0
for i in range(1, len(members)):
    if members[i] < members[i-1]:
        fumidai = members[i-1] - members[i]
        sum += fumidai
        members[i] += fumidai
 
print(sum)

