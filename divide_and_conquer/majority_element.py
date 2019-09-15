# python3

import sys

def get_majority_element(a, left, right):

    m = {}

    for i in range(n):
        # print(a[i])
        if a[i] in m:
            m[a[i]] += 1
        else:
            m[a[i]] = 1

    for key in m:
        # print(key)
        if m[key] > n/2:
            return key

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)


