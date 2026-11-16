'''Juan Jose Marin Ochoa
Codigo: 8947785'''
from sys import stdin

#heuristica de comprension de camino 
def findSet( parent, x ):
    while parent[ x ] != x:
        x = parent[ x ]
    return x

def main():
    line = stdin.readline()
    while line != '':
        n, m = map( int, line.split() )
        parent, count, sum = [], [], []
        for i in range( n+1 ): 
            parent.append( i )
            count.append( 1 )
            sum.append( i )
        #lista de padres y sus hijos 
        #rango
        for _ in range( m ):
            op = list( map( int, stdin.readline().split() ) )
            #print(op)
            if op[ 0 ] == 1:
                p, q = op[ 1 ], op[ 2 ]
                p = findSet( parent, p )
                q = findSet( parent, q )
                if p != q:
                    parent.append( len(parent) )
                    count.append( 0 )
                    sum.append( 0 )
                    new_parent = len( parent ) - 1
                    count[ new_parent ], sum[ new_parent ]  = count[ p ] + count[ q ], sum[ p ] + sum[ q ]
                    count[ p ], count[ q ], sum[ p ], sum[ q ], parent[ p ], parent[ q ] = 0, 0, 0, 0, new_parent, new_parent
            elif op[ 0 ] == 2:
                p, q = op[ 1 ], op[ 2 ]
                p = findSet( parent, p )
                q = findSet( parent, q )
                #print( op[1], op[2], p, q )
                if p != q:
                    if count[ q ] > 1:
                        count[ q ], sum[ q ] = count[ q ] + 1, sum[ q ] + op[ 1 ]
                        count[ p ], sum[ p ] = count[ p ] - 1, sum[ p ] - op[ 1 ]
                        parent[ op[ 1 ] ] = q
                    else:
                        parent.append( len(parent) )
                        count.append( 0 )
                        sum.append( 0 )
                        new_parent = len( parent ) - 1
                        count[ new_parent ], sum[ new_parent ]  = 2, op[ 1 ]+op[ 2 ]
                        count[ p ], count[ q ] = count[ p ]-1, count[ q ]-1
                        sum[ p ], sum[ q ] = sum[ p ]-op[ 1 ], sum[ q ]-op[ 2 ]
                        parent[ op[ 1 ] ], parent[ op[ 2 ] ] = new_parent, new_parent
            elif op[ 0 ] == 3:
                while parent[ op[ 1 ] ] != op[ 1 ]:
                    op[ 1 ] = parent[ op[ 1 ] ]
                print(f'{count[ op[ 1 ] ]} {sum[ op[ 1 ] ]}')
            '''if numeros[0] == 1:
                if numeros[1].isdisjoint(todos):'''
        line = stdin.readline()
main()