def phi(A, f, sol, sum, i):
    global solution, sum_final
    if i == len(A):
        if is_avl(sol):
            cost = calculate_cost(A, f, sol)
            if cost > sum_final:
                solution, sum_final = sol.copy(), cost
    else:
        phi(A, f, sol + [A[i]], sum + f[i], i + 1)
        phi(A, f, sol, sum, i + 1)
    return

def is_avl(A):
    return True

def calculate_cost(A, f, A_sub):
    return 0

def main():
    global solution, sum_final
    solution, sum_final = [], 0
    A = [1, 2, 3]
    f = [2, 3, 1]
    phi(A, f, [], 0, 0)
    if sum_final > 0:
        print(solution)
        print(sum_final)
    else:
        print("-inf")

main()
