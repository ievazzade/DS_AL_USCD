# Uses python3
import sys

def get_change(m):
    #write your code here
    m = int(m)
    return m//10 + (m%10)//5 + m%5
    
def change_iter(m):
    m = int(m)
    if m == 0:
        return 0
    num_coin = 0
    for i in [10,5,1]:
        num_coin += m//i
        m = m%i
    return num_coin


if __name__ == '__main__':
    m = input()
    print(change_iter(m))
