from sys import stdin

def textSegmentation5(S, P, N, sols, solsOpt):
    if S == 0:
        if not len(solsOpt) or len(solsOpt) > len(sols):
            solsOpt[:] = sols.copy()
    else:
        resultado = S  
        if not len(solsOpt) or len(solsOpt) > len(sols):
            for i in range(N - 1, -1, -1):
                if resultado - int(P[i]) >= 0:
                    sols.append(P[i])
                    textSegmentation5(resultado - int(P[i]), P, i + 1, sols, solsOpt)
                    sols.pop()
                

def main():
    cases = int(stdin.readline())
    cont = 0
    while cases > 0:
        cont += 1
        vals = list(map(int, stdin.readline().split()))
        n, s = vals[0], vals[1]
        p = list(map(int, stdin.readline().split()))
        solsOpt = []
        sols = []
        
        textSegmentation5(s, p, n, sols, solsOpt)
        # imprimen los datos correspondientes a la solución
        if not solsOpt:
            print(f'Case {cont}: impossible')
        else:
            print(f'Case {cont}: [{len(solsOpt)}] ' + ' '.join(map(str, sorted(solsOpt, reverse=True))))
        cases -= 1

main()