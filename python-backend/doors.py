'''Juan Jose Marin Ochoa
Codigo: 8947785'''
from sys import stdin

def binarySearchIter(v):
  low, hi = 1, v
  while hi>= low:
    mid = (hi + low) // 2
    tmp = mid *mid
    if v == tmp: return tmp
    elif v < tmp: hi = mid-1
    else: low = mid +1
  ans = (low-1)*(low-1)
  return ans

def main():
    y = int(stdin.readline())
    while y != 0:
        print(binarySearchIter(y))
        y = int(stdin.readline())
main()