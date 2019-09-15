# python3

import sys

def compute_min_refills(distance, tank, stops):

    t = tank
    all_stops = [0] + stops + [distance]
    refuels = 0
    pos = 0

    for i in range(0, len(all_stops)-1):
        if all_stops[i+1] - all_stops[i] <= t:
            if distance - pos > t:
                if pos+t < all_stops[i+1]:
                    # print(all_stops[i+1])
                    pos = all_stops[i]
                    refuels = refuels + 1
                    # print(pos, refuels)
        else:
            return -1

    return refuels


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
    
    
