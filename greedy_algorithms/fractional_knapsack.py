# Uses python3

import sys
import operator

def get_optimal_value(capacity, weights, values):

    value = 0
    c = capacity
    ratio = [values[i]/weights[i] for i in range(len(values))]
    sorted_ratio = sorted((zip(weights, values, ratio)), key=operator.itemgetter(2), reverse=True)

    for item in sorted_ratio:
        if c - item[0] >= 0:
            value = value + item[1]
            c = c - item[0]
        else:
            fraction = c/item[0]
            value = value + (fraction*item[1])
            c = c - (item[0]*fraction)

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

