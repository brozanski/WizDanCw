import sys
import math
#ZADANIA DOMOWE LISTA LAB2

# #Zad. 1
# sporty = ["Rower", "Bieganie", "Pływanie", "Piłka nożna"]
# sporty.reverse()
# sporty.append("Koszykowka")
# sporty.append("Piłka ręczna")
# print(sporty)
#
# #Zad. 2
# slownik = {"itd." : "i tak dalej",
#            "ww." : "wyzej wymienione",
#            "ds." : "do spraw"}
# print(slownik)
#
# #Zad. 3
# slownik2 = {"GTA" : "Grand Theft Auto",
#             "exp." : "Experience Points",
#             "HP" : "Health Points"}
# for a in slownik2:
#     print(a)

# #Zad. 4
# ile=0
# zdanie=input("Wpisz zdanie: ")
# for x in zdanie:
#     if x == 'a':
#         ile+=1
# print(ile)

# #Zad. 5 #jak tutaj uzyc readline i write?
# a = float(input("Podaj liczbe a: "))
# b = float(input("Podaj liczbe b: "))
# c = float(input("Podaj liczbe c: "))
# wynik = a**b + c
# print(wynik)

# #Zad. 6
# a = float(input("Podaj pierwsza liczbe: "))
# b = float(input("Podaj druga liczbe: "))
# c = float(input("Podaj trzecia liczbe: "))
# if (a > b) and (a > c):
#     maks = a
# elif (b > a) and (b > c):
#     maks = b
# else:
#     maks = c
# print("Najwieksza liczba jest ", maks)

# #Zad. 7
# liczby = [1, 2.2, 3, 4.4, 5, 6.6, 7, 8.8, 9]
# #for a in liczby:
# liczby2 = [x**2 for x in liczby]
# print(liczby2)

# #Zad. 8
# parzyste = []
# x = 0
# while x !=10:
#     x += 1
#     if x%2==0:
#         parzyste.append(x)
# print(parzyste)

# #Zad. 9
# liczba = input("Podaj liczbę nieujemną: ")
# liczba = float(liczba)
# if liczba>0:
#     print(math.sqrt(liczba))
# else:
#     print("Podana liczbę ujemną")

# try:
#     print(math.sqrt(liczba))
# except : #co tu dac
#     print("Podana liczbę ujemną")
