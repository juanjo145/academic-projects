'''Juan Jose Marin Ochoa
Codigo: 8947785'''
from sys import stdin



def encontrar(k, g, n=0):
    if n >= len(g) - 1 or g[n + 1] > k:
        return n
    return encontrar(k, g, n + 1)

def fiboDC(k, g):
    if k == 0:
        return 0
    else:
        n = encontrar(k, g)
        return (2**n) + fiboDC(k - g[n], g)

def crearfibo(f, g):
    if g[-1] >= 89999999:
        return f, g
    else:
        g.append(g[-1] + f[-1])
        f.append(f[-2] + f[-1])
        return crearfibo(f, g)



def main():
    T = int(stdin.readline())
    global f
    f, g = [1,1],[1,2]
    f, g = crearfibo(f, g)
    for _ in range(T):
        k = int(stdin.readline())
        print( format( fiboDC(k,g), 'b' ) )
main()