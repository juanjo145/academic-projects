'''Juan Jose Marin Ochoa
Codigo: 8947785'''
from sys import stdin

def main():
    y = int(stdin.readline())
    while( y !=0):
        
        tian = list(map(int, stdin.readline().split()))
        king = list(map(int, stdin.readline().split()))
        tian.sort()
        king.sort()
        # Se cambian los limites para que sean distintos 
        tmpK, tmpT = y-1, y-1
        nK, nT ,ans,flag = 0,0,0,1
        while( nT <= tmpT and nK <= tmpK and flag):
            if tian[tmpT] > king[tmpK]: 
                ans +=1
                tmpT -=1
                tmpK -= 1
            elif tian[nT] > king[nK]:
                ans += 1
                nT +=1
                nK += 1
            #Los limites se cambiaron para no tener que cambiar los 4 limites en este caso  
            elif tian[nT] < king[tmpK]:
                ans -= 1
                nT +=1
                tmpK -= 1
            else:
                 flag = False
        suma = (ans * 200 )
        print(suma)
        y = int(stdin.readline())

main()