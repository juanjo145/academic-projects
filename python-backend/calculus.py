'''Juan Jose Marin Ochoa
Codigo: 8947785'''
from sys import stdin

def main():
    y = int(stdin.readline())
    for _ in range(y):
        #el simbolo se mira en la pila 
        expresion = stdin.readline().strip()
        cant = int(stdin.readline())
        vals = list(map(int, stdin.readline().split()))
        vals.sort()
        tam = len(expresion)
        signo,despeje,res,stack = -1,0,[],[]
        res.append('+')
        for i in range(tam):
            if expresion[i] == '(':
                despeje += 1
                stack.append(signo)
                if expresion[i-1] == '-':
                    signo *= -1
                i +=1 
            elif expresion[i] == '-' and despeje >0:
                if signo == 1:
                    res.append('+')    
                    i+=1
                else:
                    res.append('-')    
                    i+=1
            elif expresion[i] == '+' and despeje >0:
                if signo == 1:
                    res.append('-')    
                    i+=1
                else:
                    res.append('+')    
                    i+=1
            elif expresion[i] == ')':
                despeje -=1
                signo = stack.pop()

            
            elif expresion[i] == '-' and despeje ==0: res.append('-')
            elif expresion[i] == '+' and despeje ==0: res.append('+')
            # print(res)
        suma,n,j =0,0,0
        while(n < cant):
            if res[n] == '+':
                suma += vals.pop()
            else: 
                suma-=vals[j]
                j +=1
            n +=1
        print(suma)
main()
