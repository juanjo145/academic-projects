'''Juan Jose Marin Ochoa
Codigo: 8947785'''
from sys import stdin

def main():
    y = stdin.readline()
    while( y !='' ):
        n = int(y)
        n = n *3
        songs,val=[],[]
        while(len(songs) < n):
            s = list(map(float,stdin.readline().split()))
            for i in range(len(s)):
                songs.append(s[i])
        #recorrido canciones diccionario[len/frecuency]=identificador
        cont,dic =0,{}
        for i in range(n):
            if cont < 3:
                if cont ==0:
                    tmp = songs[i]
                    cont +=1
                elif cont ==1:
                    l = songs[i]
                    cont +=1
                else:
                    f = songs[i]
                    #resultado ya que esto me devuelve el costo de cada cancion en la cinta  
                    dic[l/f] = tmp
                    cont =0
        #las canciones que son mas cortas y se reproducen en menos tiempo van al principio     
        dicordenado =dict( sorted(dic.items()))
        ans = int(stdin.readline()) 
        res =list(dicordenado.items())[ans-1]
        print(int(res[1]))
        y = stdin.readline()
main()