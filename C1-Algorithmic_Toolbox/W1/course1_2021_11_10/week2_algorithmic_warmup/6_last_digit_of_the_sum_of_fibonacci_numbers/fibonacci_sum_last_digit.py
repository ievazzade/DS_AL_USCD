# Uses python3
import sys
import math

def fibonacci_sum(n):
    n = ((n+2)%60)
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)%10


    return current%10-1


if __name__ == '__main__':
    input_n = input()
    n = int(input_n)
    print(fibonacci_sum(n))
