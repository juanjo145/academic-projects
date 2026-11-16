from sys import stdin
#lista de usados (lista de booleanos)
#que posicion de la lista vamos
#cuantos palitos he utilizado
    
def solv(lis,marcador,lenght,voypor,palitos,contadorSuma):
    if marcador == 0:
        if contadorSuma==0:
            marcador +=1
        
        for i in range(lenght):
                if marcador==lis[i]:
                    voypor=True
                
                palitos+=1
                #suma=lis[i]+lis[i+1]
                #recursion              

    return contadorSuma

def main():
    cases = int(stdin.readline())
    while cases != 0:
        lis = list(map(int, stdin.readline().split()))
        contadorSuma=0
        voypor=[]
        for i in range(cases):
            voypor.append(False)
        lis.sort(reverse=True)
        
        print(solv(lis,0,cases,voypor,0,contadorSuma))
        cases = int(stdin.readline())
main()