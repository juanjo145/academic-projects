INF = float('inf')

def is_elt(u, X):
    return (X & (1 << u)) != 0

def singleton(u, X):
    return X == (1 << u)

def remove_elt(u, X):
    return X & ~(1 << u)

def universe(N):
    return (1 << N) - 1

def phi_memo(N, w, u, X, mem):
    key = (u, X)
    if key in mem:
        return mem[key]
    if not is_elt(u, X):
        return INF
    if singleton(u, X):
        return w[0][u]
    Y = remove_elt(u, X)
    ans = INF
    for v in range(1, N):
        if is_elt(v, Y):
            ans = min(ans, phi_memo(N, w, v, Y, mem) + w[v][u])
    mem[key] = ans
    return ans

def tsp(N, w):
    mem = {}
    X = remove_elt(0, universe(N))
    ans = INF
    for u in range(1, N):
        ans = min(ans, phi_memo(N, w, u, X, mem) + w[u][0])
    return ans
