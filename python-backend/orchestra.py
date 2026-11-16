from sys import stdin
#cola de prioridad uso heapq
import heapq
from math import ceil

def do_heap( args,l,p,n ):
    for i in range( n ):
                #print(cont)
                cont = int( args[i] )
                heapq.heappush( l, [-cont, 1, cont] )
                p -= 1
    return p

def ordenar_part(p,l):
    while p :
                infoInstru = heapq.heappop( l )
                infoInstru[1] += 1
                infoInstru[0] = -ceil( infoInstru[2] / infoInstru[1] )
                #result = infoInstru[2] // infoInstru[1]
                #if infoInstru[2] / infoInstru[1] >= result:
                #  result += 1
                #infoInstru[0] = -result
                heapq.heappush( l, infoInstru )
                p -= 1

def main():
    
    args = stdin.readline().strip()

    while args:
        l = []
        p, n = map( int, args.split() ) 
        
        args = stdin.readline().strip().split()
        p=do_heap( args,l,p,n )
        p=ordenar_part(p,l)
        print( -heapq.heappop(l)[0] )
        args = stdin.readline().strip()

main()