def check_num(n):
    while n % 10 == 0:
        n //= 10

    num_list = []

    while n != 0:
        num_list.append(n % 10)
        n //= 10

    length = len(num_list)
    for i in range(int(length/2)):
        if num_list[i] != num_list[length-i-1]:
            print("No")
            return
    print("Yes")


n = int(input())
if n == 0:
    print("Yes")
else:
    check_num(n)
