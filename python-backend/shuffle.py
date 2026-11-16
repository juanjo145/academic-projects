def smooth_phi(x, y, z, memo={}):
    ans = None
    if len(x) + len(y) != len(z):
        ans = False

    key = (len(x), len(y))  

    if key in memo:
        ans = memo[key] 
    else:
        memo[key] = True
        if not x or not y:
            ans = all(z[i] == c for i, c in enumerate(x + y))  # Check if remaining chars match

        #Caso recursivo coinsiderando los 2 caracteres y que nos aseguremos que no halla 2 simbolos consecutivos 
        # de el mismo arreglo
        memo[key] = (
            (z[0] == x[0] and len(x) > 1 and len(y) > 1 and smooth_phi(x[1:], y, z[1:], memo))
            or (z[0] == y[0] and len(x) > 1 and len(y) > 1 and smooth_phi(x, y[1:], z[1:], memo))
            or (len(x) == 1 and z[0] == x[0] and smooth_phi([], y, z[1:], memo))
            or (len(y) == 1 and z[0] == y[0] and smooth_phi(x, [], z[1:], memo))
        )
        ans = memo[key]

    return ans
