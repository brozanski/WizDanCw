#-------------------    LAB 6   -------------------

import numpy as np

a = np.arange(2)
print(a)

#inicjalizacja tablicy
a = np.array([0, 1])
print(a)
#drugi sposób
a = np.arange(2)
print(a)

print(type(a))  #wypisanie typu zmiennej tablicy (nie jej elementów) - ndarray

print(a.dtype)  #sprawdzenie typu danych tablicy

a = np.arange(2, dtype ='int64')    #inicjalizacja tablicy z konkertnym typem danych
print(a.dtype)

b = a.astype('float')   #zapisywanie kopii tablicy jako tablicy z innym typem
print(b)
print(b.dtype)
print(b.shape)  #wypisanie rozmiaru tablicy
print(a.ndim)   # sprawdzenie ilosci wymiarow tablicy

#stworzenie tablicy wielowymiarowej może wyglądać tak
#parametrem przekazywanym do funkcji array jest obiekt, który zostanie skonwertowany na tablicę może to być Pythonowa lista
m = np.array([np.arange(2), np.arange(2)])
print(m.shape)
print(type(m))  #ponownie typem jest ndarray


#Przyklad 2
#tablice wypelnionie zerami i jedynkami
zera = np.zeros((4,4))
jedynki = np.ones((3,3))
print(zera)
print(jedynki)

print(zera.dtype)   #sprawdzenie domyslnego typu danych takich tablic
print(jedynki.dtype)


pusta = np.empty((2,2))
print(pusta)    #"pusta" macierz wcale nie jest pusta

#do elementow tablicy mozemy odwolac sie tak jak do el. np listy czyli po indeksach
poz_1 = pusta[1,1]
poz_2 = pusta[0,1]
print(poz_1)
print(poz_2)

#tworzenie macierzy 2x2 wraz z uzupełnieniem
macierz = np.array([[4,2],[3,1]])
print(macierz)

#funkcja arange potrafi także tworzyć ciągi liczb zmiennoprzecinkowych
liczby = np.arange(1,2.1,0.1)   #drugi krok = 2 daje wyniki do 1.9, a kiedy jest = 2.1 to daje wyniki do 2 !!
print(liczby)

#podobnie działa funkcja linspace, które działanie jest
# równoważne tej samej funkcji w MATLAB-ie
liczby_lin = np.linspace(1,2,5)     # od jedynki do dwojki, 5 krokow
print(liczby_lin)

#a teraz możemy utworzyć dwie macierze, najpierw wartości
#interowane są w kolumnie a następnie w wierszu
    # jak to dziala?
z = np.indices((5,4))
print(z)

#wielowymiarowe macierze możemy również generować funkcją mgrid
x, y = np.mgrid[0:5, 0:5]
print(x)
print(y)

#podobnie jak w MATLAB-ie możemy tworzyć macierze diagonalne
mat_diag = np.diag([a for a in range(4)])
print(mat_diag)

#w ponizszym przykładzie stworzony wektor wartości zostanie
#umieszczony na głównej przekątnej macierzy
#możemy podać drugi parametr funkcji diag, który określa
#indeks przekątnej względem głównej przekątnej
#która zostanie wypełniona wartościami podanego wektora
mat_diag_k = np.diag([a for a in range(5)],-1)
print(mat_diag_k)

#Numpy jest w stanie stworzyć tablicę jednowymiarową z
#dowolnego obiektu iterowalnego (iterable)
        #!!!!
z = np.fromiter(range(5), dtype='int32')
print(z)


#ciekawą funkcją Numpy jest funkcja frombuffer, dzięki której
# możemy stworzyć np. tablicę znaków
marcin = b'Marcin'
mar = np.frombuffer(marcin,dtype='S1')
print(mar)
mar_2 = np.frombuffer(marcin,dtype='S2')
print(mar_2)
#powyższa funkcja ma jednak pewną wadę dla pythona 3.x, która
#powoduje, że trzeba jawnie określić
#iż ciąg znaków przekazujemy jako ciąg bajtów co osiągamy po
#przez podanie litery 'b' przed wartością
#zmiennej tekstowej. Można podobne efekty osiągnąć inaczej

marcin = 'Marcin'
mar_3 = np.array(list(marcin))
mar_4 = np.array(list(marcin), dtype='S1')
mar_5 = np.array(list(b'Marcin'))
mar_6 = np.fromiter(marcin,dtype='S1')
mar_7 = np.fromiter(marcin,dtype='U1')
print(mar_3)
print(mar_4)
print(mar_5)
print(mar_6)
print(mar_7)


#talice w Numpy możemy w prosty sposób do siebie dodawać, odejmować, mnożyć, dzielić
mat = np.ones((2,2))
mat_1 = np.ones((2,2))
mat = mat + mat_1
print(mat)
print(mat - mat_1)
print(mat*mat_1)
print(mat/mat_1)
mat_2=5*mat_1
print(mat_2)
print(mat_2-mat_1)


#Indeksowanie i cięcie tablic - wiele sposobow - nizej przyklady

#cięcie (slicing) tablicy numpy można wykonać za pomocą wartości z funkcji slice lub range
a = np.arange(10)
print(a)
s = slice(2,7,2)
print(a[s])
s = range(2,7,2)
print(a[s])

#możemy ciąć tablice również w sposób znany z cięcia list (efekt jak wyżej)
print(a[2:7:2])
#lub tak
print(a[1:])
print(a[2:5])

#w podobny sposób postępujemy w przypadku tablic wielowymiarowych
mat = np.arange(25)
#teraz zmieniamy kształt tablicy jednowymiarowej na macierz 5x5
mat = mat.reshape((5,5))
print(mat)
print(mat[1:]) #od drugiego wiersza
print(mat[:,1]) #druga kolumna jako wektor
print(mat[:,-1:]) #ostatnia kolumna
print(mat[2:6, 1:3]) # 2 i 3 kolumna dla 3,4,5 wierszy
print(mat[:, range(2,6,2)]) # 3 i 5 kolumna
print('')


#bardziej zaawansowane, lecz trudniejsze do zrozumienia cięcia
#można osiągnąć wg. poniższego przykładu
#y będzie tablicą zawierającą wierzchołki macierzy x
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows,cols]
print(y)


#Zad.6
tekst = "la la baba ka la la"
policz1 = tekst.count(" la ")
policz2 = tekst.count("la ")
policz3 = tekst.count(" la")
print(policz1+policz2+policz3)


#ZADANIA Z PLIKU numpy_zadania

# #Zad.1
# a = np.arange(1,21)*4
# print(a)

# #Zad.2    -   dokonczyc
# liczby = np.arange(1,2.1,0.1)
# print(liczby)
# kopia = np.arange(liczby, dtype='int32')
# print(kopia)

#Zad.3
n = int(input("Podaj n: "))
a = np.ones((n,n)) * np.arange(1,n+1)

print(a)




#-------------------    LAB 7   -------------------

# #    Lab7 13.04

a = np.array(3)
b = np.array(4)

c = a+b
print(c)
print(b**2)

print(np.exp(b))
print(np.sqrt(b))
d = np.sqrt(b)
e = d+ b
print(e)    #numpy sam wybiera odpowiedni format dla siebie - zamiast int bedzie float

a = np.arange(12).reshape((3, 4))
print(a)
# print(a.sum())
# print(a.sum())
# print(a.sum(axis=0))
# print(a.sum(axis=1))
print(a.cumsum(axis=1))     #suma kumulowana


#mnozenie macierzy
a = np.arange(3)
b = np.arange(3)

print(a.dot(b))

c = np.array([[2, 3, 6], [5, 1, 3]])    #liczba kolumn w pierwszej = liczba wierszy w drugiej
d = np.array([[1,4], [2,1], [3, 5]])

e = c.dot(d)
print(e)


# a = np.arange(6).reshape(3, 2)
# print(a)
# for b in a:
#     for c in b:
#         print(b)

#krotszy zapis tego co wyzej

a = np.arange(6).reshape(3, 2)
print(a)
for b in a.flat:
    print(b)
	
	
a = np.arange(6)
print(a)
b = a.reshape((3, 2))
c = a.reshape((2, 3))
print(b)
print(c)
d = c.ravel()   #zwraca macierz wyjsciowa
print(d)
e = c.T     #Transpozycja
print(e)




import numpy as np

#Zadanie 1
a = np.array([2,3,6])
b = np.array([5,1,3])
c = a.dot(b)
print(c)
print()

#Zadanie 2  #rzad macierzy
x = np.arange(9).reshape(3,3)
y = np.arange(16).reshape(4,4)
print("Macierz x:")
print(x)
print()
print("Minimalne wartosci z macierzy x: ")
print(x.min(axis=0))
print(x.min(axis=1))
print()

print("Macierz y:")
print(y)
print()
print("Minimalne wartosci z macierzy y: ")
print(y.min(axis=0))
print(y.min(axis=1))
print()

#Zadanie 3
c = a.dot(b)
print(c)
print()

#Zadanie 4
a = np.array([2,3,6])
b = np.array([5.2,1.3,3.6])
print(a*b)

#Zadanie 5
a = np.array([[5,7,9],[4,6,8]])
print(a)
for b in a:
    b = np.sin(a)
print(b)

#Zadanie 6
a = np.array([[5,7,9],[4,6,8]])
print(a)
for b in a:
    b = np.cos(a)
print(b)

#Zadanie 7
print(a+b)

#Zadanie 8
a = np.arange(9).reshape(3,3)
for b in a:
    print(b)

#Zadanie 9
a = np.arange(9).reshape(3,3)
for b in a.flat:    #flat "splaszcza" macierz do jednej kolumny
    print(b)

#Zadanie 10
a = np.arange(9).reshape(3,3)
for b in a:
    print(b)
print()
# b.reshape(1,9)
# print(b)
# print()
# b.reshape(9,1)
# print(b)
# print()
c = a.T
print(c)
# c = ravel.c
# print(c)
print()

#Zadanie 11
a = np.arange(12)
print(a)
print()
b = a.reshape(3,4)
c = a.reshape(4,3)
d = a.reshape(2,6)
print(b)
print()
print(c)
print()
print(d)





#-------------------    LAB 8   -------------------

import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5.5, np.nan, 'a'])
print(s)
s1 = pd.Series([10, 12, 8, 14], index=['a', 'b', 'c', 'd'])     #liczba el. index musi byc taka sama jak el. serii
print(s1)

dane = {'Kraj' : ['Belgia', 'Indie', 'Brazylia'],
        'Stolica' : ['Bruksela', 'New Delhi', 'Brasil'],
        'Populacja' : [11000000, 1300000000, 220000000]}
df = pd.DataFrame(dane)
print(df)

daty = pd.date_range('20220420', periods=5)  #sami deklarujemy indexy?
df = pd.DataFrame((np.random.randn(5, 4))*10, index=daty, columns=list('ABCD'))
print(df)

df = pd.read_csv('iris.csv', header=0, sep=',',decimal='.')
print(df)
df.to_csv('nowy.csv', index=False)  #nie przekazemy indeksow do nowego pliku dzieki index=false

# xlsx = pd.ExcelFile('wyniki.xlsx',)       #czytanie plikow excela
# df = pd.read_excel(xlsx, header=0)
# print(df)
# df.to_excel('nowy.xlsx', sheet_name='Arkusz1', index=False)

print(s1['a'])
print(s1.a)

print(df['Populacja'])

print(df.iloc[[0], [0]])  #indeks wiersza, kolumny
print(df.loc[[0], ['Kraj']])  #indeks wiersza, nazwa kolumny
print(df.at[0, 'Kraj'])

print('kraj: ' + df.Kraj)


print(df.sample(10))  #losowe wiersze z dataframe
print(df.sample(10, replace=True))  #moga sie powtarzac
print(df.sample(frac=0.5))  #pobiera 50% wierszy z dataframe iris

print(df.head(10))      #10 pierwszych wierszy
print(df.tail(5))       #5 ostanich wierszy


print(s1[(s1 > 10)])
print(s1.where(s1 > 10, 'element nie spelnia warunku'))
seria = s1.copy()
seria.where(seria > 10, 'element nie spelnia warunku', inplace=True)
print(seria)
print()

print(s1[~(s1 > 10)])
print(s1[(s1 < 13) & (s1 > 8)])
print()

print(df[df['Populacja'] > 120000000])
print(df[((df.Populacja > 1000000) & (df.index.isin([0, 2])))])
print()

szukaj = ['Belgia', 'Brasil']
print(df.isin(szukaj))

s1['e'] = 15    #dodanie nowego elementu do dataframe
print(s1)

df.loc[3] = 'nowy element' #dodanie wiersza do ramki danych
print(df)
print()

df.loc[4] = ['Polska', 'Warszawa', '36000000']
print(df)
print()

df.drop(3, inplace=True)    #usuwanie wiersza
df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Pd.', 'Europa']  #dodawanie nowej kolumny
print(df)
print()

print(df.sort_values(by='Kraj'))
print()

grupa = df.groupby(by='Kontynent')
print(grupa.get_group('Europa'))
print(df.groupby('Kontynent').agg({'Populacja':['sum']}))     #agregacja - sumowanie





#-------------------    LAB 9   -------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

ts = pd.Series(np.random.randn(1000))
ts = ts.cumsum()
print(ts)
ts.plot()
plt.savefig('wykres.png')   #zeby zapisac .jpg trzeba uzyc biblioteki pillow - na egzamin
plt.show()

dane = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Dehli', 'Brasilia', 'Warszawa'],
        'Populacja' : [11000000, 1300000000, 220000000, 36000000],
        'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']}

df = pd.DataFrame(dane)
grupa = df.groupby('Kontynent').agg({'Populacja': ['sum']})

grupa.plot(kind='bar', ylabel='Populacja w mld', xlabel='Kontynent',
           rot=0, legend=True, title='Populacja dla kontynentow', color='magenta')
plt.legend(loc='upper left')
plt.show()


df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
print(df)

grupa = df.groupby('Imię i nazwisko').agg({'Wartość zamówienia': ['sum']})
grupa.plot(kind='pie', subplots=True, autopct='%.2f %%',
           fontsize=20, figsize=(6, 6))
plt.legend(loc='upper left')
plt.show()


ts = pd.Series(np.random.randn(1000))
ts = ts.cumsum()
df = pd.DataFrame(ts)
print(df)
df['Średnia krocząca'] = df.rolling(window=50).mean()
print(df)
df.plot()
plt.legend(['Wartości', 'Średnia krocząca'])
plt.show()



#Zadania z pliku 'pandas wykresy zadania.docx'

#Zadanie 1 - Stwórz wykres liniowy, który wyświetli liczbę urodzonych dzieci dla każdego roku.
xlsx = pd.ExcelFile('imiona.xlsx')      #biblioteka openpyxl
df = pd.read_excel(xlsx, header=0)

df = pd.DataFrame(df)
grupa = df.groupby('Rok').agg({'Liczba': ['sum']})
grupa.plot(kind='line', ylabel='Liczba urodzonych', xlabel='Rok',
           rot=0, legend=True, title='Liczba urodzonych dzieci dla każdego roku', color='magenta')
plt.legend(loc='upper left')
plt.show()

#Zadanie 2 - Stwórz wykres słupkowy, który wyświetli liczbę urodzonych chłopców i dziewczynek z całego zbioru.
df = pd.DataFrame(df)
grupa = df.groupby('Plec').agg({'Liczba': ['sum']})
grupa.plot(kind='bar', ylabel='Liczba urodzonych', xlabel='Płeć',
           rot=0, legend=True, title='Liczba urodzonych chłopców i dziewczynek', color='blue')
plt.legend(loc='upper left')
plt.show()      #jak zamienic 10^6 * ilosc na zwykly zapis?

#Zadanie 3 - Wykres kołowy z waściartomi % ukazującymi ilość urodzonych chłopców i dziewczynek w ostatnich 5 latach z datasetu.
grupa = df.groupby('Plec').agg({'Liczba': ['sum']})     #Jak to połączyć z zakresem lat ?
grupa.plot(kind='pie', subplots=True, autopct='%.2f %%',
           fontsize=20, figsize=(6, 6))
plt.legend(loc='upper left')
plt.show()

#Zadanie 4 - Wyświetl na pomocą wykresu słupkowego ilość złożonych zamówień przez poszczególnych sprzedawców (zbiór danych zamówienia.csv).
# df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
# df = pd.DataFrame(df)
# ilosc_zamowien = df['Sprzedawca'].value_counts
# grupa = df.groupby('Sprzedawca').agg({ilosc_zamowien: ['sum']})
# grupa.plot(kind='bar', ylabel='Liczba złożonych zamówien', xlabel='Sprzedawca',
#            rot=0, legend=True, title='ilość złożonych zamówień przez poszczególnych sprzedawców', color='blue')
# plt.legend(loc='upper left')
# plt.show()





#-------------------    LAB 10   -------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
from PIL import Image


# Listing 1
import matplotlib.pyplot as plt
#bardzo prosty wykres liniowy
plt.plot([1, 2, 3, 4])
plt.ylabel('jakieś liczby')
plt.show()


# Listing 2
#Style wektorów
# przekazujemy dwa wektory wartości, najpierw dla wektora x, następnie dla wektora y
# #dodatkowo mamy tutaj przekazywany parametr w postaci stringa, który określa styl wykresu #dla pełnej listy sprawdź dokumentację pod adresem #https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-')
#tutaj określamy listę parametrów w postaci [xmin, xmax, ymin, ymax]
plt.axis([0, 6, 0, 20])
plt.show()
#możemy też ustawić różne kolory dla poszczególnych elementów nakładając na siebie dwa wykresy
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o')

plt.axis([0, 6, 0, 20])
plt.show()


# Listing 3
#bazowy wektor wartości
t = np.arange(0., 5., 0.2)

#za pomocą pojedynczego wywołania funkcji plot() możemy wygenerować wiele wykresów na jednym płótnie (ang. canvas) #każdorazowo podając niezbędne wartości: wartości dla osi x, wartości dla osi y, styl wykresu, ...
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.legend(labels=['liniowa', 'kwadratowa', 'szescienna'])
plt.show()


# Listing 4
x = np.linspace(0, 2, 100)

#wykresy mogą być też dodawane do płótna definicja po definicji zamiast w pojedynczym wywołaniu funkcji plot()
#tutaj użyty został również parametr label, który określa etykietę danego wykresu w legendzie
plt.plot(x, x, label='liniowa')
plt.plot(x, x**2, label='kwadratowa')
plt.plot(x, x**3, label='sześcienna')

#etykiety osi
plt.xlabel('etykieta x')
plt.ylabel('etykieta y')

#tytuł wykresu
plt.title("Prosty wykres")

#włączamy pokazanie legendy
plt.legend()
plt.savefig('wykres matplot.png')

plt.show()
im1 = Image.open('wykres matplot.png')
im1 = im1.convert('RGB')
im1.save('nowy.jpg')


# Listing 5
x = np.arange(0, 10, 0.1)
s = np.sin(x)
plt.plot(x, s, label="sin(x)")
# etykieta osi
plt.xlabel('x')
plt.ylabel('sin(x)')
# tytuł wykresu
plt.title('Wykres sin(x)')
# umieszczamy legendę na wykresie
plt.legend()
plt.show()


#Listing 6

#dane w postaci słownika, ale równie dobrze może to być Pandas DataFrame
data = {'a': np.arange(50),
 'c': np.random.randint(0, 50, 50),
 'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

# #aby w ten sposób przekazać parametry wykresu należy dodać
# niezbędny parametr data, który zawiera dane dostępne poprzez
# etykiety
# #to oznacza, że 'a' jest równoważne data['a'] itd. Parametr c
# to skrót od color, tutaj przekazywany w formie wektora
# wartości kolorów dla każdej kolejnej wartości wykresu.
# Parametr s to scale - określa rozmiar, w tym przypadku punktu,
# dla
#każdej kolejnej wartości wektora wykresu. Reasumując dla
# pierwszego punktu wykresu będą brane poniższe wartości

print(f"""a={data['a'][0]}, b={data['b'][0]}, c={data['c'][0]},
d={data['d'][0]}""")
plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('wartość a')
plt.ylabel('wartość b')
plt.show()


# 3. PODWYKRESY

# Listing 7

x1 = np.arange(0, 2, 0.02)
x2 = np.arange(0, 2, 0.02)

y1 = np.sin(2 * np.pi * x1)
y2 = np.cos(2 * np.pi * x2)

plt.subplot(2, 1, 1,)
plt.plot(x1, y1, '-')
plt.title('wykres sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
ax = plt.subplot(2, 1, 2)
plt.plot(x2, y2, 'r-')

plt.xlabel('x')
plt.ylabel('cos(x)')
plt.title('wykres cos(x)')
plt.subplots_adjust(hspace=0.5)
plt.show()


# Listing 8
x1 = np.arange(0.0, 2.0, 0.02)
x2 = np.arange(0.0, 2.0, 0.02)
y1 = np.sin(2 * np.pi * x1)
y2 = np.cos(2 * np.pi * x2)

fig, axs = plt.subplots(3, 2, )
axs[0, 0].plot(x1, y1, '-')
axs[0, 0].set_title('wykres sin(x)')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('sin(x)')

axs[1, 1].plot(x2, y2, 'r-')
axs[1, 1].set_title('wykres cos(x)')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('cos(x)')

axs[2, 0].plot(x2, y2, 'r-')
axs[2, 0].set_title('wykres cos(x)')
axs[2, 0].set_xlabel('x')
axs[2, 0].set_ylabel('cos(x)')

fig.delaxes(axs[0, 1])
fig.delaxes(axs[1, 0])
fig.delaxes(axs[2, 1])
plt.show()


# Listing 9
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
        'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
        'Populacja': [11190846, 1303171035, 207847528, 38675467]}
df = pd.DataFrame(data)
print(df)

plt.bar(data=df, x='Kontynent', height='Populacja',
color=['red', 'green', 'yellow'])
plt.xlabel('Kontynenty')
plt.ylabel('Populacja w mld')
plt.show()


# Listing 10

x = np.random.randn(10000)

# bins oznacza ilość "koszy" czyli słupków, do których mają wpadać wartości z wektora x
# facekolor oznacza kolor słupków
# alpha to stopień przezroczystości wykresu
# density oznacza czy suma ilości zostanie znormalizowana do rozkładu prawdopodobieństwa (czyli przedział 0, 1)
plt.hist(x, bins=50, facecolor='g', alpha=0.75, density=True)

plt.xlabel('Wartości')
plt.ylabel('Prawdopodobieństwo')
plt.title('Histogram')
#wyświetlanie siatki
plt.grid()
plt.show()


# Listing 11

df = pd.read_csv('dane.csv', header=0, sep=";",decimal=".")
print(df)
seria = df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum()
wedges, texts, autotext = plt.pie(x=seria, labels=seria.index, autopct=lambda pct: "{:.1f}%".format(pct), textprops=dict(color="black"), colors=['red', 'green'])

plt.title('Suma zamówień dla sprzedawców')
plt.legend(loc='lower right')
plt.ylabel('Procentowy wynik wartości zamówienia')
plt.show()




# ZADANIA MATPLOTLIB.DOCX

# Zadanie 1
#Na wykresie wyświetl wykres liniowy funkcji f(x) = 1/x dla x ϵ [1, 20]. Dodaj etykietę do linii wykresu i wyświetl legendę. Dodaj odpowiednie etykiety do osi wykresu (‘x’, ’f(x)’) oraz ustaw zakres osi na (0, 1) oraz (1, długość wektora x).

x = np.arange(1, 20, 1)
f = (1/x)
plt.plot(x,f)
plt.ylabel('f(x)')
plt.xlabel('x')
plt.legend(labels =['f(x) = 1/x'])
plt.title('Wykres funkcji f(x) dla x [1, 20]')
plt.axis([1, 20, 0, 1])
plt.show()


# Zadanie 2
# Zmodyfikuj wykres z zadania 1 tak, żeby styl wykresu wyglądał tak jak na poniższym zrzucie ekranu.
# https://matplotlib.org/2.1.2/api/_as_gen/matplotlib.pyplot.plot.html

x = np.arange(1, 20, 1)
f = (1/x)
plt.plot(x,f, 'g:^')  # 'g' - green
plt.ylabel('f(x)')
plt.xlabel('x')
plt.legend(labels =['f(x) = 1/x'])
plt.title('Wykres funkcji f(x) dla x [1, 20]')
plt.axis([0, 20, 0, 1])
plt.show()


# Zadanie 3
# Na jednym wykresie wygeneruj wykresy funkcji sin(x) oraz cos(x) dla x ϵ [0, 30] z krokiem 0.1. Dodaj etykiety i legendę do wykresu.

x = np.arange(0, 30, 0.1)

y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1)
plt.plot(x, y2)

plt.legend(labels=['sin x', 'cos x'], loc='upper right')
plt.xlabel='x'
plt.ylabel='y'
plt.title('Wykres sinusa i cosinusa w x [0,30]')

plt.show()



# Zadanie 4 - na kolosie przedzialy wektorow beda podane w nawiasach otwartych lub zamknietych !
df = pd.read_csv('iris.csv', header=0, sep=',',decimal='.')
x = df['sepal length']
y = df['sepal width']
c = np.random.randint(1,50,150)
s = np.abs(x - y)
# https://matplotlib.org/3.5.0/tutorials/colors/colormaps.html
plt.scatter(x, y, c=c, s=s)
plt.show()


# Zadanie 5
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)

df = pd.DataFrame(df)
grupa = df.groupby('Plec').agg({'Liczba': ['sum']})
grupa.plot(kind='bar', ylabel='Liczba urodzonych', xlabel='Płeć',
           rot=0, legend=True, title='Liczba urodzonych chłopców i dziewczynek w całym okresie', color='blue')
plt.legend(loc='upper left')
plt.show()





#-------------------    LAB 11   -------------------

import pandas as pd
import numpy as np
import math
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns


#biblioteka seaborn
#wykres liniowy
sns.set(rc={'figure.figsize': (8,8)})
sns.lineplot(x=[1,2,3,4], y=[1,4,9,16],
             label='linia nr1', color='red',
             marker='o', linestyle=':')
sns.lineplot(x=[1,2,3,4], y=[2,5,10,17],
             label='linia nr2', color='green',
             marker='^', linestyle=':')
plt.xlabel('oś x')
plt.ylabel('oś y')
plt.title('Wykres liniowy')
plt.show()


#drugi wykres liniowy
s = pd.Series(np.random.randn(1000))
s = s.cumsum()
sns.set()
wykres = sns.relplot(kind='line', data=s, label='linia')
wykres.fig.set_size_inches(8,6)
wykres.fig.suptitle("Wykres liniowy losowych danych")
wykres.set_xlabels('indeksy')
wykres.set_ylabels("wartosci")
wykres.add_legend()
wykres.figure.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9) #parametr left nie moze miec wartosci wiekszej niz right - tak samo bottom wzgledem top
plt.show()

#roznica miedzy relplot a lineplot


#trzeci wykres liniowy
sns.set()
df = pd.read_csv('iris.csv', header=0, sep=',', decimal='.')
print(df)
wykres = sns.lineplot(data=df, x=df.index, y='sepal length', hue='class', palette=['red', 'purple', 'blue'])
wykres.set_xlabel('indeksy')
wykres.set_title('Wykres liniowy danych z Iris')
wykres.legend(title='Rodzaj kwiatu')
plt.show()


#wykres punktowy
sns.set()
data = {'a': np.arange(10),
        'c': np.random.randint(0, 50, 10),
        'd': np.random.randn(10)}
data['b'] = data['a'] + 10 * np.random.randn(10)
data['d'] = np.abs(data['d']) * 100
print(data['c'])
print(data['d'])
df = pd.DataFrame(data)
plot = sns.relplot(data=df, x='a', y='b',
                   hue='c', palette='magma', size='d', legend=True) #rozne palette - np. bright, cubehelix 
plot.fig.set_size_inches(6,6)
plot.set(xticks=data['a'])
plt.show()

#na kolosa wykres punktowy lub liniowy z seaborna - wszyskie nazwy etykiet musza byc widoczne


#wykres kolumnowy
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Dehli', 'Brasilia', 'Warszawa'],
        'Populacja' : [11000000, 1300000000, 220000000, 36000000],
        'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']}
df = pd.DataFrame(data)
sns.set()
plot = sns.barplot(data=df, x='Kontynent', y='Populacja',
                   ci=None, hue='Kontynent', estimator=np.sum,      #Estimator - jak dziala - sumowanie elementow w grupach
                   dodge=False, palette=['red', 'green', 'yellow'])
plot.legend(title='Populacja na kontynentach')
plot.set(title='Wykres słupkowy')
plt.show()


#matplotlib 3d, wykres liniowy	- na kolokwium nie bedzie 3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
print(type(ax))
t = np.linspace(0, 2 * np.pi, 100)
z = t
x = np.sin(t)*np.cos(t)
y = np.tan(t)
ax.plot(x, y, z, label='Zadanie 1')
ax.legend()
plt.show()

#sns.catplot 




#DOKONCZYC (z pdfa):
np.random.seed(19680801)


for c,m,zlow,zhigh in [('r', 'o',-50,-25)],
def randrange

ax.set_ylabel('Y Label')
ax.set_xlabel('X Label')
ax.set_zlabel('Z Label')
ax.view_init(elev=10, azim=-35)
plt.show()


#Wiele wykresów w jednym wykresuie
form mpl_toolkits.mplot3d.axes3d import get_test_data

#szerokosc 2 razy wieksza niz wysokosc
fog = plt.figure(figsize=plt.figaspect(0.5))

# pierwszy wykres

#osie dla pierwszego wykresu

ax = fig.add_subplot(1, 2, 1, projection='3d')
np.random.seed(19680801)
def randrange(n, vmin, vmax):
    '''Funkcja wspomagająca może tworzyć macierz losowych ...'''


ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

#drugi wykres

#osie dla drugiego wykresu

ax = fig.add_subplot(1, 2, 2, projection='3d')
X, Y, Z = get_test_data()
ax.plot_wireframe (X,Y,Z, rstride=10, cstride=10)
plt.show()



#Dwa typy wykresow na jednej przestrzeni - dokonczyc
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
x = np.linspace(0,1,100)
y = np.sin(x * 2 * )


colors=('r', 'g', 'b', 'k')
np.random.seed(19680801)



#Na kolosa: wykres liniowy, siatka (!!!)
	#pandas, numpy (grupy, wektory - stworzenie i umieszczenie na wykresie)
	#nawiasy kwadratowe - obydwa krance wchodza do wektora!
	#biblioteki z pliku requirements;
	#wykres koumnowy, kolowy - agregacja
