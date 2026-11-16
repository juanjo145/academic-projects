
from sys import stdin

'''Para cada caso de prueba:
    Leer el número de receptores/transmisores
    Leer las coordenadas de los sensores
    Calcular la distancia entre cada par de sensores
    Ordenar las distancias en orden ascendente
    Inicializar la ECD actual con un valor muy grande
    Para cada distancia en orden ascendente:
        Si la distancia es menor o igual que la ECD actual, no se hace nada
        De lo contrario, se actualiza la ECD actual con la distancia actual
    Imprimir la ECD actual (redondeada hacia arriba)'''





def main():
    cases = int(stdin.readline())
    while cases > 0:
        vals = []
        transmisores = int(stdin.readline())
        line=stdin.readline().split()
        while line[0] != '-1':
            while line:
                elemento = line.pop(0)
                vals.append(int(elemento))
            line=stdin.readline().split()
        cont=0
        
            
        
        # imprimen los datos correspondientes a la solución

        cases -= 1

main()