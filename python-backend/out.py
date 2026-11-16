'''Juan Jose Marin Ochoa
Codigo: 8947785'''
from sys import stdin

numbers, N,sumaTodos = [],4,0

def solve(n, res, numerosUsados, sumaUsados, total):
    global numbers,N,sumaTodos
    ans = False
    if(n == N):
        if(res == 23):
            ans = True
    else:
        #num [operacion] (tot - sum):  solucionActual-> res  y la suma de los numeros que me falta por ver
        if((res >= 23 and res - (total - sumaUsados) <= 23) or (res < 23 and (res + (total - sumaUsados) >= 23 or res * (total - sumaUsados) >= 23))):
            i = 0
            while(i < 5 and not ans):
                if(i not in numerosUsados):
                    
                    numerosUsados.append(i)
                    sumaUsados += numbers[i]
                    #if resta == True:
                    ans = solve( n + 1, res - numbers[i], numerosUsados, sumaUsados, total)
                    #print(ans)
                    #suma
                    if(not ans):
                        ans = solve(n + 1, res + numbers[i], numerosUsados, sumaUsados, total)
                    #multiplicacion
                    if(not ans):
                        ans = solve( n + 1,res * numbers[i], numerosUsados, sumaUsados, total)
                    numerosUsados.pop(-1)
                    #print(numerosUsados)
                    sumaUsados -= numbers[i]
                i += 1
    return ans

def main():
    global numbers,N,sumaTodos
    Y = stdin.readline()
    while(Y != "0 0 0 0 0\n"):
        numbers = list(map(int, Y.split()))
        num = 0
        ans = False
        sumaTodos = sum(numbers)
        numbers.sort(reverse=True)
        if(sumaTodos == 23):
            ans = True
        while(num < 5 and not ans):
            ans = solve(0, numbers[num], [num], numbers[num], sum(numbers))
            num += 1 
        if(ans):
            print("Possible")
        else:
            print("Impossible")
        Y = stdin.readline()

main()