'''Juan Jose Marin Ochoa
Codigo: 8947785'''
from sys import stdin
def solve(hippos, N, H, Ta, Td):
    hippos.sort()
    izq, der,tiempo = 0, N - 1,0
    while izq <= der:
        total_height = hippos[izq] + hippos[der]
        if total_height < H and izq != der:
            tiempo += Td 
            izq += 1
            der -= 1
        else:
            tiempo += Ta
            der -= 1
    return tiempo
def main():
    read = stdin.readline
    cases = int(read().strip())
    numCase = 1
    while cases:
        N, H, Ta, Td = map(int, read().strip().split())
        hippos = [int(x) for x in read().strip().split()] #list( map( int, stdin.readline().spli()) )
        if (Ta << 1) >= Td:
            ans = solve(hippos, N, H, Ta, Td)
        else:
            ans = N*Ta
        print("Case {}: {}".format(numCase, ans))
        numCase += 1
        cases -= 1

main()