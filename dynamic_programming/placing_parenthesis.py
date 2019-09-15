# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinMax(i, j, s, M, m):

    min_val = []
    max_val = []
    for k in range(i, j):
        m1 = evalt(M[i][k], M[k+1][j], s[k])
        m2 = evalt(M[i][k], m[k + 1][j], s[k])
        m3 = evalt(m[i][k], M[k + 1][j], s[k])
        m4 = evalt(m[i][k], m[k + 1][j], s[k])

        min_val.append(min(m1, m2, m3, m4))
        max_val.append(max(m1, m2, m3, m4))

    return (min(min_val), max(max_val))


def get_maximum_value(dataset):

    d = [int(dataset[i]) for i in range(len(dataset)) if i % 2 == 0]
    n = len(d)
    sym = [dataset[i] for i in range(len(dataset)) if i % 2 != 0]

    M = [[0] * len(d) for _ in range(n)]
    m = [[0] * len(d) for _ in range(n)]

    for i in range(len(d)):
        m[i][i], M[i][i] = d[i], d[i]

    for x in range(1, n):
        for i in range(0, n - x):
            j = i + x
            m[i][j], M[i][j] = MinMax(i, j, sym, M, m)

    return M[0][n-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))


# a = '5-8+7*4-8+9'
# d = [int(a[i]) for i in range(len(a)) if i % 2 == 0]
# n = len(d)
# sym = [a[i] for i in range(len(a)) if i % 2 != 0]
#
# M = [[0]*len(d) for _ in range(n)]
# m = [[0]*len(d) for _ in range(n)]
#
# for i in range(len(d)):
#     m[i][i], M[i][i] = d[i], d[i]
#
# for x in range(1, n):
#     for i in range(0, n-x):
#         j = i + x
#         m[i][j], M[i][j] = MinMax(i, j, sym)
