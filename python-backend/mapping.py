from sys import stdin

def maping(lis, cont,N):
    
    orden = esta_ordenada(lis,N)
    if orden==True:
        cont += 1
        
    else:
        for i in range(N - 1):
            if lis[i] > lis[i + 1]:
                lis[i], lis[i + 1] = lis[i + 1], lis[i]
                
                cont=maping(lis, cont,N)
                lis[i], lis[i + 1] = lis[i + 1], lis[i]
    return cont

def esta_ordenada(lista,N):
    for i in range(1, N):
        if lista[i] < lista[i - 1]:
            return False
    return True

def main():
    N, *lis = map(int, stdin.readline().split())
    contador=1
    while len(lis) != 0:
        if N != 0:
            cont = 0
            if not esta_ordenada(lis,N):
                cont=maping(lis, cont,N)
            
            print(f"There are {cont} swap maps for input data set {contador}.")
            contador +=1
        N, *lis = map(int, stdin.readline().split())

main()