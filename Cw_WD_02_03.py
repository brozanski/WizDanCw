Cwiczenia Python 02.03

import math
print(math.pow(math.log(5+math.pow(math.sin(8), 2)), 1/6))

liczba_szesnstkowa = 0x1f
print('{0:x}'.format(liczba_szesnstkowa))

if warunek1 - instrukcja lub blok instrukcji gdy ten warunek1 jest spelniony
elif warunek2 - instrukcja lub blok instrukcji gdy ten warunek2 jest spelniony
else - instrukcje gdy warunki niespelnione

x==y ; x!=y ; x>y ; x<y ; x>=y ; x<=y


	ZADANIE NA POROWNANIE
a = 8
b = 7

if a == b:
    print('liczba a jest rowna liczbie b')
else:
    print('liczba a nie jest rowna liczbie b')
##############
if a > b:
	print('liczba a jest wieksza od liczby b')
elif a < b:
	print('liczba a jest mniejsza od liczby b')
else:
	print('liczby sa rowne')
##############
if a == b:
    print('liczba a jest rowna liczbie b')
elif a>b:
    print('liczba a jest wieksza od liczby b')
else:
    print('liczba a jest mniejsza od liczby b')
	
	
	
	ZADANIE NA WCZYTYWANIE I RZUTOWANIE
a = input('podaj liczbe: ')
print(a)
print(type(a))
a = int(a)  #rzutowanie ze string na int
print(a)
print(type(a))
# if (a>b) & (c>d):

a = input('podaj liczbe a: ')
b = input('podaj liczbe b: ')
c = input('podaj liczbe c: ')
d = input('podaj liczbe d: ')

a=int(a)
b=int(b)
c=int(c)
d=int(d)
if (a>b) & (c>d):
    print("a jest wieksze od b i c jest wieksze od d")
else:
    print("a jest mniejsze od b lub c jest mniejsze od d")
	
	
	
	PETLE
for licznik in sekwencja	- instrukcja lub 
else 	- instrukcja lub instrukcje po zadeklarowaniu petli

#############
for a in range(0, 7, 1):
    print(a)
##############	
lista = ["cos", 4, 5, 6.5]
for a in lista:
    print(a)
else:
    print("wyswietlono wszystkie elementy z listy")
###############
while warunek	- instrukcja lub blok instrukcji
else	- moze byc ale nie musi
###############
licznik = 0
while licznik != 11:
    print(licznik)
    licznik += 1
###############
lista = [4, 8, 5, 3, 2, 9, 7]
licznik = 0
liczba =input("Wpisz liczbe calkowita: ")
while licznik != len(lista):
    if int(liczba) - lista[licznik] == 0:
        print('Liczba ' + str(liczba) + ' - ' + str(lista[licznik]) + ' =0')
        break
    else:
        licznik += 1
else:
    print("Zadna z wartosci nie dala odpowiedniego wyniku")
###############
lista1 = [4, 6, 8, 1, 6, 7, 2, 9]
lista2 = [4, 7, 3, 5]
suma=[]
for a in lista1:
    for b in lista2:
        wynik = a+b
        suma.append(wynik)
    print(suma)
###############
	WYKRYWANIE BLEDOW
try - instrukcje ktore moga zawierac jakis blad
	except nazwa_bledu - instrukcje po wykruciu bledu
	except nazwa_bledu
	else - wyniki w ktorych nie ma bledow
	
	
a = input("Podaj pierwsza liczbe: ")
b = input("Podaj druga liczbe: ")
try:
    a=int(a)
    b=int(b)
    wynik = a/b
    print (wynik)
except ZeroDivisionError:
    print("Nie mozna dzielic przez 0")
except ValueError:
    print("Nie wczytano liczby calkowitej")
###############
https://docs.python.org/3/tutorial/datastructures.html

lista=['a',5,5.6,[1,2,3]]	
{1:10, 'a', 'b', 1:20} <-- 1:20 nadpisze 1:10

slownik={klucz:wartosc}
		\			 /
	  1 element slownika
slownik[klucz]
slownik[nowy klucz]=wartosc dla nowego klucza


append, insert, extend, pop, remove, clear, del, sort, revers

lista1=[4, 5, 1, 44, 14]
lista1.sort()
print(lista1)

lista1.insert(1, 5) #pierwsza liczba w nawiasie to pozycja na liscie, druga liczba to wartosc ktora chcemy insertowac
lista1.sort()
print(lista1)

lista1.append(1) #dodaje na koniec listy
print(lista1)
lista1.append(1984)
print(lista1)

lista2=[100,1000,10000]
lista1.extend(lista2)
print(lista1) #printuje liste po rozszerzeniu

lista1.pop(4) #usuwa element z danego indeksu - indeksy zaczynaja sie od 0
print(lista1)

lista1.remove(1000) #usuwa element o wartosci podanej w nawiasie
print(lista1)

lista1.clear()
print(lista1)
