import numpy as np
from numba import njit


H, W = list(map(int, input().split(" ")))
grid = np.zeros((H, W), bool)
for h in range(H):
    grid[h] = np.array(list(input())) == "#"


@njit
def main():
    X = np.zeros((H, W))
    Y = np.zeros((H, W))
    Z = np.zeros((H, W))
    DP = np.zeros((H, W))
    DP[0][0] = 1
    M = 10 ** 9 + 7
    for i in range(0, H):
        for j in range(0, W):
            if grid[i][j]:
                continue
            if j == 0 and i == 0:
                continue
            if j > 0:
                X[i][j] = (X[i][j-1] + DP[i][j-1]) % M
            if i > 0:
                Y[i][j] = (Y[i-1][j] + DP[i-1][j]) % M
            if i > 0 and j > 0:
                Z[i][j] = (Z[i-1][j-1] + DP[i-1][j-1]) % M
            DP[i][j] = (X[i][j] + Y[i][j] + Z[i][j]) % M
    print(int(DP[H-1][W-1]))


if __name__ == "__main__":
    main()
