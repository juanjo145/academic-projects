def solve(n, m,T):
    if T == 0 :
        m += 1
    elif T > 0:
        while n < N:
            if T- X[n] >= 0:
                m = solve(n + 1, m, T - X[n])
            n += 1
    return m

X = [1, 2, 3, 4, 5, 6, 7]
T = 10
N = len(X)
print(solve(0, 0, T))
