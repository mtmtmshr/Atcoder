import heapq


q_num = int(input())

num_list = []
result = []
sk = 0
for i in range(q_num):
    tmp = list(map(int, input().split()))
    if len(tmp) == 1:
        print(heapq.heappop(num_list)+sk)
        continue
    sousa, num = tmp
    if sousa == 1:
        heapq.heappush(num_list, num-sk)
    elif sousa == 2:
        sk += num
