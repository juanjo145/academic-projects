def phi(X, W, T, sol, sum, i):
    global solution, sum_final
    if T == 0:
        if sum > sum_final:
            solution, sum_final = sol.copy(), sum
    else:
        if T > 0 and i >= 0:
            sol.append(W[i])
            phi(X,W, T-X[i], sol, sum+W[i], i-1)
            sol.pop()
            phi(X,W, T, sol, sum, i-1)
    return

def main():
    global solution, sum_final
    sum_final, solution = 0, []
    X, W, T = [3,2,5,1,1], [5,2,4,3,1], 10
    phi(X,W,T,[], 0, len(X)-1)
    if sum_final > 0: print(solution)
    else: print("-inf")
main()