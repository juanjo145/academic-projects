'''Juan Jose Marin Ochoa
Codigo: 8947785'''
import heapq
from sys import stdin

def main():
    read = stdin.readline
    cases = int(read().strip())
    
    while(cases):
        n, k =map(int, read().strip().split())
        cont,cola,mapa =1,[],{}
        while(n):
            #mapa
            clave, valor = stdin.readline().split()
            mapa[clave] = [cont,int(valor)]
            heapq.heappush(cola,(mapa[clave][1],mapa[clave][0],clave))
            cont +=1
            n -=1
        cont2 = 0 
        flag = 0
        while(cont2 < k):
            t, f, m = heapq.heappop(cola)
            cont2 += 1
            heapq.heappush(cola,(t+mapa[m][1], f, m))
            print(t, m)
        cases -=1
main()
