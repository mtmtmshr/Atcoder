import numpy as np


if __name__ == "__main__":
    n, w = list(map(int, input().split(" ")))
    water = np.zeros((2*10**5+10, 1), int)
    for _ in range(n):
        s, t, p = list(map(int, input().split(" ")))
        water[s] += p
        water[t] -= p
    if np.max(np.cumsum(water)) <= w:
        print("Yes")
    else:
        print("No")
