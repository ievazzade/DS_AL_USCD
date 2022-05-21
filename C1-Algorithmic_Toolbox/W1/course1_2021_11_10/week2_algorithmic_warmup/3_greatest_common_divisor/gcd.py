# Uses python3
import sys

def gcd_fast(a, b):
    if b == 0:
        return a
    return gcd_fast(b, a%b)

if __name__ == "__main__":
    input_n = input()
    a, b = map(int, input_n.split())
    print(gcd_fast(a, b))
