'''Juan Jose Marin 
Codigo de estudiante : 8947785'''
from sys import stdin
import math
def phi(letras,N,L,C):
    ans,total,linea  =0,0,1
    for i in range(N):
        if total+letras[i] <=C:total +=letras[i]+1
        else:
            linea +=1
            total=letras[i]+1
    ans= math.ceil(linea/L)
    return ans
def main():
    Y = stdin.readline()
    while Y != "":
        N,L,C = map(int, Y.split())
        #L es el numero maximo de lineas por pagina 
        #C es el numero maximo de caracteres por linea
        lineas = stdin.readline().strip()
        palabras = lineas.split()
        numLetras =[]
        for palabra in palabras:
            conteo = len(palabra)
            numLetras.append(conteo)
        print(phi(numLetras,N,L,C))
        Y = stdin.readline()
main()