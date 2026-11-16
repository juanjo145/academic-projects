from sys import stdin


def main():
    contador = 0
    resul =[]
    data = []
    args = int(stdin.readline())
    #Le entrego el numero de casos
    for case in range(args):
        n,t,m = list(map(int,stdin.readline().split(' ')))
        #n, t, m = map(int, input().split(' '))
        carros =[]
        for case in range(m) :
            carros.append(stdin.readline().split())
        contador=0
        tiempo = int(carros[0][0])
        copia = carros.copy()
        posicion = 'left'
        while len(carros) > 0:
            espacio = 0
            contador = 0
            if int(carros[0][0]) > tiempo and posicion == carros[0][1]:
                tiempo = int(carros[0][0])
            elif int(carros[0][0]) > tiempo and posicion != carros[0][1]:
                tiempo = int(carros[0][0] ) + t
                posicion = carros[0][1]
            print(carros)
            #longCarros=len(carros)    
            while contador < len(carros) and espacio < n and tiempo >= int(carros[contador][0]):
                if posicion == carros[contador][1]:
                    espacio = espacio + 1
                    copia[copia.index(carros[contador])] = tiempo + t
                    del carros[contador]
                    contador -= 1
                contador +=1
            if posicion == 'left':
                posicion = 'right'
            else : 
                posicion = 'left'
            tiempo = tiempo + t
        resul.append(copia)
    for i in resul :
        contador = contador + 1
        for j in i:
            print(j)
        if contador < args:
            print( '\n', end ="" )
main()
