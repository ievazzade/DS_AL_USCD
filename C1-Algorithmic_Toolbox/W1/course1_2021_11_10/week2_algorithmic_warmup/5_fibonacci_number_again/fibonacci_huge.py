# Uses python3
import sys

def get_fibonacci(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current \
        = current, (previous + current) % m
        
         
        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1

def get_fibonacci_huge(n, m):
    pP = pisanoPeriod(m)
    return get_fibonacci(n%(pP), m)

if __name__ == '__main__':
    input_n = input();
    n, m = map(int, input_n.split())
    print(get_fibonacci_huge(n, m))

