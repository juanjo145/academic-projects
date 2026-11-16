from sys import stdin

def main():
    k = int(stdin.readline())
    i = 0
    while i < k:
        n = int( stdin.readline())
        amigos=[]
        unicas=[]
        lista =[]
        contador = 0
        for j in range (n):
            args = list(map(int,stdin.readline().split()))
            m = args[0]
            stamps = args[1:]
            amigos.append((m, stamps))
        sets = [set(x[1]) for x in amigos]
        unique_elements_per_set = [s.difference(*[x for i, x in enumerate(sets) if i != j]) for j, s in enumerate(sets)]
        #for j in range(unique_elements_per_set):
        t = 0
        for conjunto in unique_elements_per_set:
            t = t +(len(conjunto))

        print(f'Case {i+1}: ', end="")
        temp = len(unique_elements_per_set)
        tmp =0
        for conjunto in unique_elements_per_set:
            res = (len(conjunto)/t)
            tmp +=1
            resultado = "{:.6f}%".format(res * 100)
            if tmp == temp:
                print(resultado)
            else:
                print(resultado, end=" ")
            #res = " ".join("{}%".format(resultado) )
        
        
        i += 1
main()