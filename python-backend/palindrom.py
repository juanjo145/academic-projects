from sys import stdin
import sys

sys.setrecursionlimit (10**4)

def solve(seq, flag, termino,count,K):
    if count >K:
        return count

    if flag >= termino or count>K:
        return 0
    if seq[flag] == seq[termino]:
        return solve(seq, flag + 1, termino - 1,count,K)
    else:
        count +=1
        primero = solve(seq, flag + 1, termino,count,K)
        segundo = solve(seq, flag, termino - 1,count,K)
        if primero < segundo:
            return primero + 1
        else:
            return segundo + 1
    
         


def main():
    T = int(stdin.readline())
    for t in range(T):
        n, k = map(int, stdin.readline().split())
        seq = list(map(int, stdin.readline().split()))
        difficulty = solve(seq,0,(n-1),0,k)
        if difficulty == 0:
            print(f'Case {t + 1}: Too easy')
        elif difficulty > k:
            print(f'Case {t + 1}: Too difficult')
        else:
            print(f'Case {t + 1}: {difficulty}')

main()