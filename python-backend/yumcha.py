from sys import stdin
import math
N, x, T, K = None, None, None, None

def solve(acumulate, mem, dims, sum_favour, i, cant_dishes):
    ans, ans1, ans2 = 0, 0, 0
    if i == K: ans = 0
    elif (i, cant_dishes, acumulate) in mem: 
        return mem[ (i, cant_dishes, acumulate) ]
    else:
        sum = (dims[i][0])*1.1
        if (acumulate+sum)/(N+1) <= x and cant_dishes+1 <= 2*(N+1):
            ans1 = solve(acumulate+sum, mem, dims, sum_favour, i+1, cant_dishes+1)+sum_favour[i]
        if (acumulate+(2*sum))/(N+1) <= x and cant_dishes+2 <= 2*(N+1):
            ans2 = solve(acumulate+(2*sum), mem, dims, sum_favour, i+1, cant_dishes+2)+2*sum_favour[i]
        ans = solve(acumulate, mem, dims, sum_favour, i+1, cant_dishes)
        ans = max(ans, ans1, ans2)
    mem[ (i, cant_dishes, acumulate) ] = ans
    return ans

def main():
    global N, x, T, K
    N, x, T, K = map(int,stdin.readline().split())
    while N != 0 and x != 0 and T != 0 and K != 0:
        dims = [ list(map(int, stdin.readline().split())) for _ in range(K) ]
        sum_favour = [ sum(dims[i][1:]) for i in range(K) ]
        print("{:.2f}".format(solve(T*(N+1)*(1.1),{},dims,sum_favour,0, 0)/(N+1)))
        N, x, T, K = map(int,stdin.readline().split())
main()