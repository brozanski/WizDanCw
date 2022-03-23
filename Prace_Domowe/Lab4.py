import sys
import math
#PRACA DOMOWA LAB4

# #Zad.1
# liczby=[]
# for x in range(0,31):
#     liczby.append(x * 2)
# file = open("pomnozone.txt", "w+")
# file.write(str(liczby))
# file.close()

# #Zad.2
# with open('pomnozone.txt', 'r') as plik:
#     for linia in plik:
#         print(linia, end='')

# #Zad.3
# print("Wpisz kilka linijek tekstu")
# linijki = sys.stdin.readline()
# plik = open('linijki.txt', 'w+')
# plik.write(linijki)
# plik.close()
#
# with open('linijki.txt', 'r') as plik:
#     for linia in plik:
#         print(linia, end='')


# #Zad.4
# class NaZakupy():
#     """Zakupy"""
#     nazwa_produktu = ""
#     ilosc = 0
#     jednostka_miary = ""
#     cena_jed = 0
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#             self.nazwa_produktu = nazwa_produktu
#             self.ilosc = ilosc
#             self.jednostka_miary = jednostka_miary
#             self.cena_jed  = cena_jed
#
#     def wyswietl_produkt(self):
#         print(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed)
#     def ile_produktu(self):
#         print(str(self.ilosc) + " " + self.jednostka_miary)
#     def ile_kosztuje(self):
#         kwota = self.cena_jed * self.ilosc
#         print(kwota)
# zakup = NaZakupy("Ziemniaki",3,"kg",2)
# zakup.wyswietl_produkt()   #dlaczego wyrzuca błąd?
# zakup.ile_produktu()
# zakup.ile_kosztuje()


# #Zad. 6
# class Robaczek:
#     x = 0
#     y = 0
#     krok = 1
# 
#     def __init__(self, x, y, krok):
#         self.x = x
#         self.y = y
#         self.krok = krok
# 
#     def idz_w_gore(self, ile_krokow):
#         self.y += (ile_krokow * self.krok)
#     def idz_w_dol(self, ile_krokow):
#         self.y -= (ile_krokow * self.krok)
#     def idz_w_prawo(self, ile_krokow):
#         self.x += (ile_krokow * self.krok)
#     def idz_w_lewo(self, ile_krokow):
#         self.y -= (ile_krokow * self.krok)
# 
#     def pokaz_gdzie_jestes(self):
#         print("Robaczek znajduje się na współrzędnych x = " + str(self.x) + " i y =" + str(self.y))
# 
# ruch = Robaczek(0, 0, 1) #pozycja startowa i wielkosc kroku robaczka
# 
# ruch.idz_w_prawo(3)
# ruch.idz_w_lewo(7)
# ruch.idz_w_gore(1)
# ruch.idz_w_dol(2)
# ruch.pokaz_gdzie_jestes()
