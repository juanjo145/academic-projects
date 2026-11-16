from sys import stdin

def main():
    n = stdin.readline(  )
    #res={}
    while n != "":
        n = int( n )
        res = {}
        maximo = 0
        #lectura de los datos incluyendo ya la verificacion de donde esta el valor maximo
        for i in range( n ):
            vals=int( stdin.readline() )
            maximo = max( maximo, vals )
            if vals not in res:
                res[ vals ] = 0
            res[ vals ] += 1
        
        #el siguiente paso es calcular la mediana
        valM = n // 2
        med = []
        #variables semiglobales   
        bandera = True
        
        cont = 0 # num contado
        i = 0
        totalRan = 0
        impPar = n % 2 != 0 # impar o par
        # Bucle para cada posible valor de A
        while i <= maximo:

            # Si el valor de A no está en la entrada, pasar al siguiente valor de A
            if i in res and res[ i ] > 0:
                # Incrementar el número de elementos contados
                cont = cont + res[ i ]

                # Si todavía no se ha encontrado la primera mediana 
                # y se han contado al menos la valor medio de los números,
                #  guardar la primera mediana
                if bandera and cont >= valM:
                    bandera = False
                    med.append( i )

                    # Si el número de elementos en la entrada es par, contar el número de elementos iguales a la primera mediana
                    if not impPar:
                        totalRan += res[ i ]

                # Si se ha encontrado la primera mediana y se han contado más de la valor medio de los números, guardar la segunda mediana y salir del bucle
                if cont >= valM + 1:
                    if impPar or i != med[ 0 ]:
                        totalRan += res[ i ]
                    med.append( i )
                    i = maximo + 1 # Salir del bucle
                    # break # Esta línea ya no es necesaria
                    
            i += 1 # Incrementar i

        if impPar:
            print( med[ 1 ], totalRan, 1 )
        else:
            j = 1 if med[ 0 ] == med[ 1 ] else med[ 1 ] - med[ 0 ] + 1
            print(med[ 0 ], totalRan, j)

        #print(mean)

        # imprimir la solución
        
        n = stdin.readline()

main()
