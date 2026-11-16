from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)
'''La tecnica de dividir y conquistar asegura que todas las posibles ubicaciones 
de los puentes se coinsideren de una manera mas optima ya que al hacer esto tambien dividimos el problema
por partes para asi ser mas optimo por ende utilizar dividir y conquistar es importante en este ejercicio
tambien si dividimos el problema en partes baja la complejidad'''



def phi(columna, C, B, S, distancias, mem):
    ans = None
    #1 CASO BASE que pase por todas las columnas y me quedan puentes por construir 
    if (columna >= C and B != 0): ans = 1e18
    elif B == 0: ans = 0
    elif (columna,B) in mem: ans = mem[(columna,B)]
    else:
        if(((B-1)*S)+columna < C and B >1) or B==1:
            ans = distancias[columna]+phi(columna+S+1, C, B-1, S, distancias, mem)
        
        if ((B-1)*S)+columna+B < C:
            ans = min( ans, phi(columna+1, C, B, S, distancias, mem) )
        mem[(columna,B)] = ans
    return ans

def imprimir_mapa(mapa):
    print("---------------------------------------")
    for fila in mapa:
        print(''.join(fila))
    print("---------------------------------------")
    print()
        
#lastS posicion mas arriba de la costa
'''La función verifica si el nodo actual es un bloque de tierra (‘#’) y
si está dentro de los límites del arreglo. Si es así, lo marca como ‘S’ para indicar que ha sido 
visitado y actualiza lastS[col] con la fila más baja de tierra encontrada en la columna col. Luego,
la función se llama a sí misma en las cuatro direcciones: arriba, abajo, izquierda y derecha. 
Esto permite explorar todas las celdas conectadas que son bloques de tierra. La función se detiene 
cuando encuentra una celda que no es un bloque de tierra o que está fuera de los límites del arreglo3'''
def dfs(fila, columna, R, C, lastS, mapa):
    if not (fila < 0 or columna < 0 or fila >= R or columna >= C or mapa[fila][columna] != '#'):
        mapa[fila][columna] = 'S'
        #imprimir_mapa(mapa)
        dfs( fila, columna + 1, R, C, lastS, mapa)#derecha
        #imprimir_mapa(mapa)
        dfs( fila + 1, columna, R, C, lastS, mapa)#abajo
        #imprimir_mapa(mapa)
        dfs( fila, columna - 1, R, C, lastS, mapa)#izquierda
        #imprimir_mapa(mapa)
        dfs( fila - 1, columna, R, C, lastS, mapa)#arriba
        lastS[columna] = min(lastS[columna], fila)#lagos
        
def main():
    Y = stdin.readline()    
    while Y != '':
        numeros = list(map(int, Y.split()))
        R, C = numeros[0], numeros[1] #fila y columnaumna
        # B = Numero de puentes a construir 
        # S = Numero de espacios que separa cada puente
        B, S = map(int, stdin.readline().split())
        distancias, lastS = [0] * (C), [1001] * (C)
        mapa = [list(input().strip()) for _ in range(R)]
        #print("entrada")
        #imprimir_mapa(mapa)
        #print("salida")
        dfs( R-1, 0, R, C, lastS, mapa )
        imprimir_mapa(mapa)
        #i en este caso seria la distancia que hay de la ultima S hasta el la primera fila
        print(lastS)
        for columna in range(C):
            #i es el valor de la ubicacion de la ultima s en la columna que estamos
            i = lastS[columna]
            while i > 0 and mapa[i][columna] != '#':
                i-=1
            #Se restan -1 porque la ultima costa no se tiene en cuenta en la distancia por ende tambien se cuenta y 
            #se tiene que descontar
            distancias[columna] = lastS[columna] - i - 1
        print(distancias)
        print( phi(0, C, B, S, distancias, {}) )
        Y = stdin.readline() 
main()