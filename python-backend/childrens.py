'''Juan Jose Marin 
Codigo de estudiante : 8947785'''
from sys import stdin

def solve(numbers, N, i, tmp_result):
    global result
    if i == -1:
        if tmp_result > result:
            result = str(tmp_result)
    else:
        h = numbers[i]
        numbers.pop(i)
        tmp = str(tmp_result)
        # comparacion de strings da v o f concatenando
        if tmp_result+h > h+tmp_result:
            tmp += h
        else:
            tmp = h+tmp
        solve(numbers, N, len(numbers)-1, tmp)
        numbers.append(h)
        solve(numbers, N, i-1, tmp_result)
    return
def main():
    N = int( stdin.readline() )
    while N != 0:
        global result
        result = ' '
        numbers = list( stdin.readline().split())
        numbers = sorted(numbers, key = lambda x : int(x))
        solve(numbers, N, N-1, '')
        print(result)
        N = int( stdin.readline() )
main()