'''Juan Jose Marin Ochoa
Codigo: 8947785'''
from sys import stdin

def main():
    t = int (stdin.readline())
    
    for cont in range(t):
        #X del empresario y Y es lo que le da al jefe
        profit, res = [],0
        n, k = map(int, stdin.readline().split())
        X = list(map(int, stdin.readline().split()))
        Y = list(map(int, stdin.readline().split()))
        for i in range(n): 
                val = Y[i] - X[i]
                profit.append(val)
        profit.sort()
        while( n != 0 ):
                
                if profit[n-1] >= 0:res += profit[n-1]
                else:
                    if n > k:res += profit[n-1]
                n -= 1
        cont +=1
        if res > 0:print("Case {}: {}".format(cont, res))
        else: print("Case {}: No Profit".format(cont))
        
        
main()        
