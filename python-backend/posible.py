from cmath import inf
from sys import stdin

h = -1
sur = 0
B = []

def poda(A, m, mT, s, d):
    cnt, ans = 0, True
    
    if m >= 4:
        for i in range(m - 4, m + 1):
            if A[i] == s:
                cnt = cnt + s
            else:
                cnt = cnt - d

        if cnt >= 0:
            ans = False
        else:
            ans = True
    
    return ans

def bug(s, d, M, m, t, A):
    global h, sur, B
    if m == M:
        if h == -1:
            h = sur
            B = list(A)
    else:
        if m < len(A):
            bug(s, d, M, m + 1, t, A)
        else:
            A.append(s)
            if poda(A, m, m + 4, s, d):
                bug(s, d, M, m + 1, t + s, A)
            A[m] = d
            t = t - d
            sur = sur + 1
            if poda(A, m, m + 4, s, d):
                bug(s, d, M, m + 1, t, A) 
    
def main():
    global h, sur, B
    s = (stdin.readline().split())
    while len(s) != 0:
        sur = 0
        h = -1
        s[0], s[1] = int(s[0]), int(s[1])
        bug(s[0], s[1], 12, 0, 0, [])
        sT = s[0] * (12 - h) - s[1] * h
        tmp = 0
        for i in range(len(B)):
            if B[i] == s[0]:
                tmp = tmp + s[0]
            else:
                tmp = tmp - s[1]
        if tmp < 0:
            print("Deficit")
        else:
            print(tmp)
        s = (stdin.readline().split())

main()