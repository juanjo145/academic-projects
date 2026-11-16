'''Juan Jose Marin Ochoa
stockMarket.py'''
import sys
from sys import stdin
sys.setrecursionlimit(2**29)

def solve( p, descuento, i, mem, status ):
    if i == len(p): 
        return 0
    if (i,status) in mem: 
        return mem[ (i, status) ]
    else:
        if status == 0: 
            result = max( solve( p, descuento, i+1, mem, status ), solve( p, descuento, i+1, mem, 1 )-p[i] )
        else: 
            result = max( solve( p, descuento, i+1, mem, status ), solve( p, descuento, i+1, mem, 0 )+(p[i]-descuento) )
    mem[ (i, status) ] = result
    return result
def main():
    Y = stdin.readline()
    
    while Y != '':
        N, C = map(int, Y.split())
        P = list(map(int, stdin.readline().split()))
        #maxi =0
        #phiMemo(C, N,P,maxi, mem=[],i=0,compraVenta=[])
        ans = solve( P, C, 0, {}, 0)
        print(ans)    
        Y = stdin.readline()
main()
