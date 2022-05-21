# Uses python3
import sys

def lcm(a, b):
    gcd_ab = gcd(a, b)
    return int(a*b/gcd_ab)

def gcd(a, b):
    if b == 0:
        return a
    return int(gcd(b, a%b))


if __name__ == '__main__':
    input_n = input()
    a, b = map(int, input_n.split())
    print(lcm(a, b))

