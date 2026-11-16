'''Juan Jose Marin Ochoa
Codigo: 8947785'''
from sys import stdin

def main():
    y = int(stdin.readline())
    for _ in range(y):
        p, n = map(int,stdin.readline().split())
        amigos = list(map(int, stdin.readline().split()))
        lis = []
        for i in range(n):
            lis.append((i,amigos[i]))
        #ordena de menor a mayor viendo cuales son menores x[1]
        #ordena de mayor a menor si son iguales -x[0]
        lis.sort(key=lambda x:(x[1],-x[0]))
        tamaño,dic = n,{}
        #ver quien paga que segun las reglas
        for clave in range(tamaño):
            total = p //n
            n -=1
            if total >= lis[clave][1]:

                p -= lis[clave][1]
            else:
                #resultado si lo que tiene que pagar es mayor a lo que tiene para pagar    
                lis[clave] = (lis[clave][0],total)
                    
                p -=total
        if p == 0:
            for i in range(tamaño):
                dic[lis[i][0]]= lis[i][1]
            valores = " ".join(map(str, dict(sorted(dic.items())).values()))
            print(valores)

        else:print("IMPOSSIBLE")

main()