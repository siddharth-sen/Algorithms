# Uses python3
import sys

def get_change(m):
    coin = 0
    # change = [4, 3, 1]

    while m > 0:
        if m % 3 == 0 and m % 4 != 0:
            m = m - 3
            coin += 1
        else:
            if m >= 4:
                m = m - 4
                coin += 1
            elif m >= 3:
                m = m - 3
                coin += 1
            else:
                m = m - 1
                coin += 1

    return coin

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

