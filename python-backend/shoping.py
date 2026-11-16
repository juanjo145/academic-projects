'''Juan Jose Marin Ochoa
Codigo: 8947785'''
from sys import stdin
INF = float('inf')
# Función para calcular todas las distancias más cortas entre todas las parejas de nodos
def floyd_warshall(graph, n):
    # Inicializar la matriz de distancias
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in graph:
        dist[u][v] = w
        dist[v][u] = w  # El grafo es no dirigido

    # Aplicar Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist
#funciones de mascaras
def is_elt(u, X):
    return (X & (1 << u)) != 0

def singleton(u, X):
    return X == (1 << u)

def remove_elt(u, X):
    return X & ~(1 << u)

def universe(N):
    return (1 << N) - 1



def phi_memo(dist,stores,memo,n,pos, bitmask):
        ans = INF
        # Caso base: todos los nodos han sido visitados
        if bitmask == universe(n):
            ans = dist[stores[pos]][0]  # Regresar a casa
        # Retornar valor ya calculado
        elif memo[pos][bitmask] is not None:
            ans = memo[pos][bitmask]
        else:
        # Probar todos los nodos que aún no han sido visitados
            for v in range(1,n):
                #is_elt()
                if bitmask & (1 << v) == 0:
                    ans = min(ans, phi_memo(dist,stores,memo,n,v, bitmask | (1 << v)) + dist[stores[pos]][stores[v]])
            # Guardar en la tabla de memorización
            memo[pos][bitmask] = ans
        return ans

def main():
    y = int(stdin.readline())
    for _ in range(y):
        intersecciones, tiendas = [], []
        # intersecciones y caminos
        i, c = map(int, stdin.readline().split())
        for _ in range(c):
            # intersecciones X, Y se conectan por D
            X, Y, D = map(int, stdin.readline().split())
            intersecciones.append((X, Y, D))
        t = int(stdin.readline())
        for _ in range(t):
            t1 = int(stdin.readline())
            tiendas.append(t1)
        # Calcular todas las distancias más cortas
        dist = floyd_warshall(intersecciones, i)
        # Resolver TSP con programación dinámica
        stores = [0]+tiendas
        n = len(stores)
        # Crear tabla de memorización
        memo = [[None] * (1 << n) for _ in range(n)]
        result = phi_memo(dist,stores,memo,n,0, 1)
        print(result)

main()
