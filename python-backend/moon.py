'''Juan Jose Marin Ochoa
Codigo: 8947785'''
from sys import stdin

def biseccion(f, a, b, v):
  low, hi, ans = a, b, None
  eps = 1e-6
  iter = 0
  while hi - low > eps:
    mid = (hi + low) / 2
    if v <= f(mid): hi = mid
    else: low = mid
    iter += 1
  ans = low
  return ans

def f(t):
   return T*t-D

def main():
    global S,D,T
    y = int(stdin.readline())
    for _ in range(y):
        T, S, D = map(int, stdin.readline().split())
        T, D =(T *86400), D * 1000000
        print("Tiempo y distancia convertidos:",T,D)
        if D ==0 : print(f"Add {0} tons")
        #limite a-1000000, limite b 1000000
        else:
          a,b = -99999999,99999999
          ans =biseccion(f,a,b,0)
          ans = int(ans)
          if ans >0:print(f"Remove {ans} tons")
          else: 
            ans = ans *-1 
            print(f"Add {ans} tons")
main()