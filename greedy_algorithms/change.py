# python3

import sys

def get_change(m):

    money = m
    change = [10, 5, 1]
    coin = 0

    for c in change:
        if int(money/c) > 0:
            coin = coin + int(money/c)
            money = money - (c*int(money/c))
            # print(coin, money)

    return coin

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

