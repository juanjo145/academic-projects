'''Juan Jose Marin Ochoa
Codigo: 8947785
Codigo de honor: Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
a seguir los más altos estándares de integridad académica.'''
from sys import stdin

'''
    Entrada:
        - A (lista de tuplas): Lista de tuplas (inicio, fin) que representan los intervalos de tiempo.
        - i (entero): Índice actual en la lista de intervalos.
        - X (entero): Tiempo objetivo para construir la hamburguesa.
        - actual (entero): Tiempo actual acumulado.
        - mem (diccionario): Diccionario para almacenar resultados previamente calculados.
        - Y (entero): Número total de intervalos.

    Salida:
        ans(entero): El número mínimo de pasos para construir la hamburguesa perfecta o 99999 si no es posible.

    Objetivo:
        El objetivo de esta función es determinar el número mínimo de volteos necesarios para asar
        una hamburguesa perfecta. Se consideran los tiempos de cocción y los intervalos disponibles 
        para voltear la carne.Si no es posible construir la hamburguesa en el tiempo objetivo, se devuelve 99999.
    '''
def solve(A, i, X, actual, mem,Y):
    ans = None
    if i > 0 and i != Y:
        # 
        actual += A[i][0]-A[i-1][1]
    if i == Y:
        #ladoO: lado opuesto a la parrilla, es el que no esta sobre la parrilla  
        ladoO = A[i-1][1]-actual
    else:
        ladoO = A[i][0]-actual
    if ladoO == X or actual == X:
        if ladoO == X: 
            ans = 0
        else: 
            ans = 1
    elif ladoO > X or actual > X or i == Y: 
        ans = 99999
    elif (actual,i) in mem: 
        ans = mem[(actual,i)]
    else:
        #
        ans = min(1+solve(A, i+1, X, ladoO, mem,Y),solve(A, i+1, X, actual+(A[i][1]-A[i][0]), mem,Y))
        #print(actual)
        for j in range((A[i][1]-A[i][0])-1,-1,-1):
            ans = min(ans, 1+solve(A, i+1, X, (A[i][1]-(actual+j)), mem,Y),
                      2+solve(A, i+1, X, actual+j, mem,Y))
    mem[(actual,i)] = ans
    return ans

def main():
    Y = int(stdin.readline())
    for _ in range(Y):
        X, Y = map(int, stdin.readline().split())
        A = [tuple(map(int, stdin.readline().split())) for _ in range(Y)]
        actual = A[0][0]
        ans = solve(A, 0, X, actual, {},Y)  

        if ans == 99999: print('Another bland and poorly cooked burger!')
        else: print(f'Perfect burger!\n{ans}')
main()