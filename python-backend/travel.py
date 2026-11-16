'''Juan Jose Marin Ochoa
Codigo: 8947785'''
from decimal import Decimal, ROUND_HALF_UP
from sys import stdin

millas = 0

def solve(capacidad, gasolinaAct, costo, gas_station, i):
    global min_costo,millas
    if i == len(gas_station)-1 and costo < min_costo:
        min_costo = costo
    elif costo < min_costo:
        gasolinaFut = (gas_station[i+1][0] - gas_station[i][0]) / millas
        if gasolinaFut > gasolinaAct:
            solve(capacidad, capacidad-gasolinaFut,  costo + 2 + (round((capacidad-gasolinaAct)*gas_station[i][1]) / 100), gas_station, i+1)
        elif gasolinaAct <= capacidad/2:
            solve(capacidad, capacidad-gasolinaFut,  costo + 2 + (round((capacidad-gasolinaAct)*gas_station[i][1]) / 100), gas_station, i+1)
            solve(capacidad, gasolinaAct-gasolinaFut,  costo, gas_station, i+1)
            #print(min_costo)
        else:
            solve(capacidad, gasolinaAct-gasolinaFut, costo, gas_station, i+1)

def main():
    global min_costo,millas
    N = float(stdin.readline())
    cnt = 1
    while N != -1:
        min_costo = 999999
        capacidad, millas, costoOrg, gasolina = map(float, stdin.readline().split())
        gasolineras = []
        for _ in range(int(gasolina)):
            x, y = map(float, stdin.readline().split())
            gasolineras.append((x, y))

        gasolineras.append([N])
        solve(capacidad, capacidad-(gasolineras[0][0]/millas),costoOrg, gasolineras, 0)
        #min_costo_decimal = Decimal(min_costo/100).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
        print(f'Data Set #{cnt}')
        print(f'minimum cost = ${min_costo:.2f}')
        N = float(stdin.readline())
        cnt += 1
main()