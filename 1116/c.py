import copy


def go_city(n, k, t_city, went_city, time):
    count = 0
    if len(went_city) == n:
        time += t_city[went_city[0]][went_city[-1]]
        if time == k:
            return 1
        else:
            return 0
    for i in range(n):
        if i not in went_city:
            wented = copy.deepcopy(went_city)
            wented.append(i)
            count += go_city(n, k, t_city, wented, time+t_city[i][went_city[-1]])
    return count


if __name__ == "__main__":
    n, k = list(map(int, input().split(" ")))
    t_city = []
    for _ in range(n):
        t_city.append(list(map(int, input().split(" "))))
    went_city = [0]
    time = 0
    count = go_city(n, k, t_city, went_city, time)
    print(count)
