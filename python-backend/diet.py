'''Juan Jose Marin Ochoa
Codigo: 8947785'''
from sys import stdin


INFI = 2500*101
#limite para que no me de 0 si no es menor al limite no se puede.
def knapsackMemo(m, n, mem):
    ans = None
    if (m, n) in mem: ans = mem[(m, n)]
    else:
        if m <= 0: ans = 0
        elif n == 0: ans =INFI
        else: 
            ans = min( knapsackMemo(m - W[n - 1], n - 1, mem) + W[n - 1], knapsackMemo(m, n - 1, mem))
        mem[(m, n)] = ans
    return ans


def main():
    y = int(stdin.readline())
    
    for _ in range(y):
        global W
        n = int(stdin.readline())#Minimo de monto de calorias
        p = int(stdin.readline())
        y = stdin.readline()
        W = [int(x) for x in y.split()]
        W.sort()
        ans =(knapsackMemo(n,p,{} ))
        if ans == INFI: print("NO SOLUTION")
        else: print(ans)
main()
        
    