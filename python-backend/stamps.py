from sys import stdin
'''el tamaño de la emvoltura restringe el numero de esteampillas que se usan en un envoltorio'''

def phi(n,C,stamps):
    ans = None
    return ans

def impresion(ansV,ans):
    ansV.sort(key=lambda x: len(x))
    for i in range(len(ansV)-1):
        if len(ansV[i]) == len(ansV[i+1]):
            for j in range(len(ansV[i])):
                if ansV[i][-(1+j)] > ansV[i+1][-(1+j)]:
                    return ans, ansV[i+1]
                elif ansV[i][-(1+j)] < ansV[i+1][-(1+j)]:
                    return ans, ansV[i]
        else:
            return ans, ansV[i]
    return ans, ansV[0]



def main():
    S = int (stdin.readline())
    while S!=0:
        vals = []
        n= int(stdin.readline())
        for i in range(n):vals.append(list(map(int, stdin.readline().split())))
        ans = 0
        #ans v = [arreglo de respueta ], ans es el resultado de la funcion phi+
        ansV = [phi(n,S,vals[i])  for i in range(n) ]
        #phi(n,S,vals)
        impresion(ansV,ans)
        print(ansV,ans)
        print(f"max coverage = {ans:3d} :", end="")
        print("{:3d}".format(ansV[0]), end="")
        for i in range(1, len(ansV)):
            print(" {:2d}".format(ansV[i]), end="")
        print()

        S= int (stdin.readline())

    

main()
