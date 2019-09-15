# Uses python3
import sys
import random
import operator


# def pivot(a):
#     m = {}
#     for i in range(len(a)):
#         if a[i] in m:
#             m[a[i]] += 1
#         else:
#             m[a[i]] = 1
#     m = sorted(m.items(), reverse=True, key=operator.itemgetter(1))
#     return m[0][0]

#
# def partition3(a, l, r):
#     # a = [2, 5, 4, 1, 0]
#     x = a[l]
#     left, right, mid = [], [], []
#     p1, p2 = 0, 0
#
#     for item in a[l:r+1]:
#         if item < x:
#             left.append(item)
#             p1 += 1
#         elif item > x:
#             right.append(item)
#         elif item == x:
#             mid.append(item)
#             p2 += 1
#
#     a = left+mid+right
#     print(a)
#     return p1, p1+p2


def partition3(a, l, r):
    x = a[l]
    begin = l + 1
    end = l

    for i in range(l + 1, r + 1):
        if a[i] <= x:
            end += 1
            a[i], a[end] = a[end], a[i]
            if a[end] < x:
                a[begin], a[end] = a[end], a[begin]
                begin += 1

    a[l], a[begin - 1] = a[begin - 1], a[l]

    return [begin, end]


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    [m1, m2] = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

