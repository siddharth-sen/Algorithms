# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result


def optimal_weight_dp(W, w):

    g = [[0] * (n + 1) for _ in range(W + 1)]

    for i in range(1, len(w) + 1):
        for weight in range(1, W + 1):
            g[weight][i] = g[weight][i - 1]
            # print((i, weight))
            if w[i - 1] <= weight:
                gold = g[weight - w[i - 1]][i - 1] + w[i - 1]
                if g[weight][i] < gold:
                    g[weight][i] = gold

    return g[W][len(w)]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight_dp(W, w))


