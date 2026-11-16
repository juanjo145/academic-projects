from sys import stdin

def solve(N, ultima, posibles, ficha, i):
    global flag
    #print(ficha)
    if i == N+1 and ficha[1] == ultima[0] : flag = 'YES'
    else:
        if flag == 'NO':
            for j in range(len(posibles)):
                if posibles[j] != None and posibles[j][0] == ficha[1]:
                    tmp = posibles[j]
                    posibles[j] = None
                    solve(N, ultima, posibles, tmp, i+1)
                    posibles[j] = tmp
                elif posibles[j] != None and posibles[j][1] == ficha[1]:
                    tmp = (posibles[j][1], posibles[j][0])
                    posibles[j] = None
                    solve(N, ultima, posibles, tmp, i+1)
                    posibles[j] = tmp
    return

def main():
    N = int(stdin.readline())
    while(N!=0):
        global flag
        flag = 'NO'
        M = int(stdin.readline())
        posibles =[]
        primera = tuple(map(int, stdin.readline().split()))
        ultima = tuple(map(int, stdin.readline().split()))    
        for i in range(M):
            cadena = stdin.readline()
            numeros = [int(x) for x in cadena.split()]
            tupla = tuple(numeros)
            posibles.append(tupla)
        solve(N, ultima, posibles, primera, 1)
        print(flag)
        N = int(stdin.readline())
main()