'''Juan Jose Marin Ochoa
Codigo: 8947785'''
from sys import stdin

def fn(n):
    ans = 0
    if n == 0: ans =0
    else:ans= (n %10)+ fn(n // 10)
    return ans
def fg(n):
    ans = 0
    if n <=9 : ans = n 
    else:ans =fg(fn(n))
    return ans

def main():
    n = int(stdin.readline())
    while n != 0:
        print (fg(n))
        n = int(stdin.readline())
main()