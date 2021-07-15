import numpy as np
import math

def silnia():
    a = int(input('Podaj liczbe, ktorej silnie mam obliczyć: '))
    x = 1
    for i in range (1,a+1):
        x = x * i
    print('Silnia = ', x)


def gra():
    a = int(input('Podaj liczbe od 0 do 9: '))
    x = np.random.randint(0, 10)
    while (a != x):
        if a > x:
            print('za duzo!')
        elif a < x:
            print('za malo!')
        a = int(input('Podaj liczbe od 0 do 9: '))
    else:
        print('udalo się, koniec gry!')


def pierwiastki():
    a = int(input("Podaj wspolczynnik rowniania a: "))
    b = int(input("Podaj wspolczynnik rowniania b: "))
    c = int(input("Podaj wspolczynnik rowniania c: "))
    delta = (b * b) - (4 * a * c)
    print('delta =', delta)
    if delta > 0:
        x1 = -b - math.sqrt(delta) / (2 * a)
        x2 = -b + math.sqrt(delta) / (2 * a)
        print("x1 = ", x1)
        print("x2 = ", x2)
    else:
        if delta == 0:
            x = -b / (2 * a)
            print("x = ", x)
        else:
            print("brak miejsc zerowych")


def suma_liczb():
    a = int(input("Podaj liczbe calkowita a: "))
    b = int(input("Podaj liczbe calkowita b: "))
    suma = 0
    if a > b:
        for i in range(b+1, a):
            suma = suma + i
    elif a < b:
        for i in range(a+1, b):
            suma = suma + i
    else:
        print('Liczby maja taka sama wartosc!')
    print('Suma =', suma)


def dopoki_dodatnia():
    a = int(input('Podaj liczbe: '))
    suma = 0
    ilosc = 0
    srednia = 0
    while (a >= 0):
        suma = suma + a
        ilosc = ilosc + 1
        a = int(input('Podaj liczbe: '))
    else:
        print('Podales liczbe ujemna!')
        srednia = suma / ilosc
        print('Suma liczb: ', suma, ' Ilosc podanych liczb: ', ilosc, ' Srednia liczb: ', srednia)


def gwiazdki():
    a = int(input('Podaj liczbe: '))
    ilosc = 0
    for i in range(1, a+1):
        ilosc = ilosc + 1
        for j in range(ilosc):
            print('*', end = '')
        print('\n')


def podatek():
    a = int(input('Podaj kwote, od ktorej chcesz wyliczyc podatek: '))
    podatek = 0
    while a >= 0:
        if a <= 5000:
            podatek = 0
        elif (a > 5000 and a <= 15000):
            podatek = a * 0.1
        elif (a > 15000 and a <= 35000):
            podatek = a * 0.15
        elif a >= 35000:
            podatek = a * 0.2
        print('Podatek od kwoty ', a, ' wynosi: ', podatek)
        a = int(input('Podaj kwote, od ktorej chcesz wyliczyc podatek: '))
    else:
        print('Podales liczbe ujemna, koniec programu!')

# ----- SPRAWDZENIE DZIALANIA -----
# 01
#silnia()

# 02
#gra()

# 03
#pierwiastki()

# 04
#suma_liczb()

# 05
#dopoki_dodatnia()

# 06
#gwiazdki()

# 07
#podatek()