'''Juan Jose Marin 
Codigo de estudiante : 8947785'''
from sys import stdin
import heapq
import time



def main():
    Y = int(stdin.readline())
    for x in range(Y):
        #ini = time.time()
        v =stdin.readline()
        n = int(stdin.readline())
        #tons, dates = [ tuple(map(int, stdin.readline().split())) for _ in range(n) ]
        orders = [ tuple(map(int, stdin.readline().split())) for _ in range(n) ]
        orders = sorted(orders, key=lambda x: x[1])

        queue,total_tons= [],0
        for order in orders:
            total_tons += order[0]
            heapq.heappush(queue, -order[0])
            while total_tons > order[1]:
                n-=1
                total_tons += heapq.heappop(queue)
        
        if x == Y-1 : print(n)
        else:print(n, end='\n\n')
        #fini = time.time()
        #print(fini-ini)

main()