password = input()

strong = True
def isStronPassword(password):
    start = password[0]
    next_num = int(start)+1
    same_flag = True
    seq_flag = True
    for i in password[1:]:
        if next_num >= 10:
            next_num %= 10
        if i != start:
            same_flag = False
        if int(i) != next_num:
            seq_flag = False
        next_num += 1
    if same_flag or seq_flag:
        return False
    return True



if isStronPassword(password):
    print("Strong")
else:
    print("Weak")