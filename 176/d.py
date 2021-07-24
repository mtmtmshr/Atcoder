import copy


h, w = map(int, input().split())
ch, cw = map(int, input().split())
dh, dw = map(int, input().split())
s = []
for i in range(h):
    s.append(list(input()))
visited = []
visited.append([ch-1, cw-1])
new_visit = [[ch-1, cw-1]]


def check_pos(s, x, y, dx, dy, visited):
    if x+dx < 0 or x+dx >= w:
        return
    if y+dy < 0 or y+dy >= h:
        return

    if s[y+dy][x+dx] == ".":
        if [y+dy, x+dx] not in visited:
            visited.append([y+dy, x+dx])
            new_visit.append([y+dy, x+dx])
            check_around(s, x+dx, y+dy, visited)


def check_around(s, x, y, visited):
    check_pos(s, x, y, 1, 0, visited)
    check_pos(s, x, y, 0, 1, visited)
    check_pos(s, x, y, 0, -1, visited)
    check_pos(s, x, y, -1, 0, visited)

def warp(x, y, visited, s):
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            if dx == 0 and dy == 0:
                continue
            if x+dx < 0 or x+dx >= w:
                continue
            if y+dy < 0 or y+dy >= h:
                continue

            if s[y+dy][x+dx] == ".":
                if [y+dy, x+dx] not in visited:
                    new_visit.append([y+dy, x+dx])
                    visited.append([y+dy, x+dx])

def second_move(visited, s):
    prev_visited = copy.deepcopy(visited)
    for visited_pos in prev_visited:
        warp(visited_pos[1], visited_pos[0], visited, s)

count = 0
is_finish = False
while not is_finish and visited:
    prev_new_visit = copy.deepcopy(new_visit)
    for visited_pos in prev_new_visit:
        check_around(s, visited_pos[0], visited_pos[1], visited)
    for visited_pos in new_visit:
        if visited_pos[0]+1 == dh and visited_pos[1]+1 == dw:
            print(count)
            is_finish = True
            break
    new_visit = []
    second_move(visited, s)
    count += 1
    if not new_visit and not is_finish:
        print("-1")
        is_finish = True

