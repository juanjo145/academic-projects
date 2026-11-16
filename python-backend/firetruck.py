'''Juan Jose Marin Ochoa
Codigo: 8947785'''
from sys import stdin
def solve(node, N, grafo, vistado, cerca):
    global result
    vistado[node] = True
    if node == N:
        result += 1
        for i in range(len(cerca)):
            if i == len(cerca)-1:
                #print(grafo)
                print(cerca[i])
            else:
                print(cerca[i], end = ' ')
    else:
        for i in grafo[node]:
            if vistado[i] == False:
                cerca.append(i)
                solve(i, N, grafo, vistado, cerca)
                cerca.pop()
                vistado[i] = False
    return
def main():
    N = stdin.readline()
    cnt = 1
    global result
    while N != '':
        result, N = 0, int(N)
        grafo, vistado = [], []
        for _ in range(N+1):
            grafo.append([])
            vistado.append(False)
        nodo = list(map(int, stdin.readline().split()))
        while nodo[0] != 0 and nodo[1] != 0:
            x, y = nodo[0], nodo[1]
            if x >= len(vistado)-1 or y >= len(vistado)-1:
                for _ in range(max(x,y)-(len(vistado)-1)):
                    grafo.append([])
                    vistado.append(False)
            grafo[x].append(y)
            grafo[y].append(x)
            nodo = list(map(int, stdin.readline().split()))
        grafo = [sorted(sublist) for sublist in grafo] 
        print(f'CASE {cnt}:')
        solve(1, N, grafo, vistado,[1])
        print(f'There are {result} routes from the firestation to streetcorner {N}.')
        cnt += 1
        N = stdin.readline()
main()