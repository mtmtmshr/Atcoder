import itertools
import copy
import sys


s1 = input()
s2 = input()
s3 = input()

s1_len = len(s1)
s2_len = len(s2)
s3_len = len(s3)
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

s1_s2 = []
s1t = set()
s2t = set()
s3t = set()
for i, a in enumerate(s1):
    for j, b in enumerate(s2):
        if a == b:
            s1_s2.append([i, j])
            s1t.add(i)
s1_s3 = []
for i, a in enumerate(s1):
    for j, b in enumerate(s3):
        if a == b:
            s1_s3.append([i, j])
            s1t.add(i)
            s3t.add(j)

s2_s3 = []
for i, a in enumerate(s2):
    for j, b in enumerate(s3):
        if a == b:
            s2_s3.append([i, j])
            s2t.add(i)
            s3t.add(j)


for num in itertools.permutations(num_list, s1_len):
    n1 = 0
    tmp_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i, n in enumerate(num):
        n1 *= 10
        n1 += n
        if i not in s1t:
            tmp_list.remove(n)
    for num2 in itertools.permutations(tmp_list, s2_len):
        tmp_list2 = copy.deepcopy(tmp_list)
        n2 = 0
        for i, n in enumerate(num2):
            n2 *= 10
            n2 += n
            if i not in s2t:
                tmp_list2.remove(n)
        for num3 in itertools.permutations(tmp_list2, s3_len):
            n3 = 0
            for n in num3:
                n3 *= 10
                n3 += n
            if n1 + n2 == n3:
                print(n1)
                print(n2)
                print(n3)
                sys.exit()

print("UNSOLVABLE")
