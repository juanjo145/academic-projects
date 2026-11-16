'''Juan Jose Marin Ochoa
Codigo: 8947785'''
from sys import stdin

def phi( mision, combustible, memo, t, b ):
    # Caso base: si ya hemos llegado al final de la lista de misiones, retornamos 0
    if mision == len(t):ans = 0
    # Si ya hemos calculado la respuesta para esta misión y combustible, la retornamos desde la memoria
    elif ( mision, combustible ) in memo:ans = memo[ (mision, combustible) ]
    # Si no hemos calculado la respuesta todavía, la calculamos y la almacenamos en la memoria para uso futuro
    else:
        if combustible == 0:
            ans = t[mision] + phi( mision+1, combustible+b[mision], memo, t, b )
        elif combustible > len(t)-mision:
            ans = ( t[ mision ] >> 1 ) + phi(  mision+1, combustible-1 +b[ mision ], memo, t, b )
        else:
            ans = min( t[ mision ] + phi( mision+1, combustible+b[mision], memo, t, b ),( t[ mision ] >> 1 ) + phi(  mision+1, combustible-1 +b[ mision ], memo, t, b ) )
        memo[ (mision, combustible) ] = ans
    return ans

def main():
    line =int( stdin.readline())
    while line != 0:
        t, b = [], []
        for _ in range( line ):
            ti, bi = map( int, stdin.readline().split() )
            t.append(ti)
            b.append(bi)
        ans = phi( 0, 0, {}, t, b)
        print( ans )
        line = int(stdin.readline())
main()
