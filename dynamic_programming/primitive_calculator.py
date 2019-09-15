# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def get_min_ops(n):
    result = [0]*(n+1)

    for i in range(2, n+1):
        op1 = result[i-1]
        op2 = sys.maxsize
        op3 = sys.maxsize
        if i % 2 == 0:
            op2 = result[int(i/2)]
        if i % 3 == 0:
            op3 = result[int(i/3)]
        min_ops = min(op1, op2, op3)

        result[i] = min_ops+1

    return result


def optimal_sequence_dp(n):
    sequence = []
    ops = get_min_ops(n)

    while n > 0:
        sequence.append(n)

        if n % 3 != 0 and n % 2 != 0:
            n = n - 1
        elif n % 2 == 0 and n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            if ops[n-1] < ops[n//2]:
                n = n - 1
            else:
                n = n // 2
        elif n % 3 == 0:
            if ops[n-1] < ops[n//3]:
                n = n - 1
            else:
                n = n // 3

    return reversed(sequence)


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence_dp(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
    
