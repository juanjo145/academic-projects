'''Juan Jose Marin 
Codigo de estudiante : 8947785'''
from sys import stdin

def main():
    Y = int( stdin.readline() )
    for i in range(Y):
        N, D = map( int, stdin.readline().split() )
        rocas, recorrido, maximo, ultima = [ item.split('-') for item in stdin.readline().split() ], 0, 0, 0
        flag =False
        while recorrido < N:
            # mirar si es big como ->big[0]
            if recorrido == 0 or rocas[recorrido][0] == 'B':
                #mirar si small es como small[0]
                if rocas[recorrido][0] == 'S':
                    rocas[recorrido][0] = False
                maximo  = max(maximo, int(rocas[recorrido][1])-ultima) 
                ultima = int(rocas[recorrido][1])
            #rocas[recorrido][0] == 'S'
            else:
                maximo = max(maximo, int(rocas[recorrido][1])-ultima)
                ultima = int(rocas[recorrido][1])
                rocas[recorrido][0] = False
            if recorrido+1 < N and rocas[recorrido+1][0] == 'B':
                recorrido += 1
            else: 
                recorrido+=2
        maximo, ultima = max(maximo, D-ultima), D
        #for start final y por ultimo como itera para recorrer devuelta
        for recorrido in range(N-1,-1,-1):
            if rocas[recorrido][0] != False: 
                maximo  = max(maximo, ultima-int(rocas[recorrido][1])) 
                ultima = int(rocas[recorrido][1])
        ans = max(maximo,ultima)
        print("Case {}: {}".format(i+1,ans))
main()