'''
Juan Jose Marin Ochoa
squares.py
'''
import sys
from sys import stdin
sys.setrecursionlimit(2**29)
import math

def phi(n, mem={}):
    if n == 0:
        return 0
    if n in mem:
        return mem[n]
    ans = float('inf')
    for i in range(1, int(math.sqrt(n)) + 1):
        ans = min(ans, phi(n - i * i) + 1)
    mem[n] = ans
    return ans


def main():
    t = int(stdin.readline())
    for i in range(t):
        n = int(stdin.readline())
        ans = phi(n,{})
        print(ans)
main()
