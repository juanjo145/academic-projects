'''Juan Jose Marin Ochoa
Codigo: 8947785'''
from sys import stdin
#Asembly
def main():
    y = int(stdin.readline())
    for i in range(y):
        n = int(stdin.readline())
        lista = list(map(int, stdin.readline().split()))
        i += 1
        cont,ans= 1,0
        #Los que no estan ordenados se cuentan para saber cuantos ordenar 
        for j in range(n):
            if lista[j] == cont:
                ans +=1
                cont +=1
        print("Case {}: {}".format(i, n-ans))
main()