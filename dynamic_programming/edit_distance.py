# Uses python3

import sys

def edit_distance(s, t):
    T = [[0] * (len(t)+1) for _ in range(len(s)+1)]

    for i in range(len(s)+1):
        T[i][0] = i
    for j in range(len(t)+1):
        T[0][j] = j

    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            if s[i-1] == t[j-1]:
                diff = 0
            else:
                diff = 1
            T[i][j] = min((T[i][j-1])+1,
                          (T[i-1][j])+1,
                          (T[i-1][j-1])+diff)

    return T[len(s)][len(t)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
