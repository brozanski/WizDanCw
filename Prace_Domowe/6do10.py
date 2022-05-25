#-------------------    LAB 6   -------------------

import numpy as np
# zad1
# a = np.arange(0, 4*20+1, 4)
# print(a)

# zad2
# lista = [1.5, 2.3, 4.7, 3.6, 6,7]
# a = np.array(lista)
# b = a.astype(dtype='int32')
# print(b)
# c = np.array(lista, dtype='int32')
# print(b)

# zad3
def tablica(n):
    a = np.zeros((n*n), dtype='int32')
    for i in range(0, len(a)):
        a[i] = 2**i
    tab = a.reshape((n, n))
    return tab

print(tablica(5))

# zad4
def generuj(liczba, ilosc):
    return np.logspace(1, ilosc, num=ilosc, base=liczba)

print(generuj(2,4))

# zad5
def diagonalna(n):
    a = np.arange(n, -1, -1)
    diag = np.diag(a, 2)
    return diag

print(diagonalna(4))

# zad6
malina = np.array(list('malina'))
mrowka = np.array(list('mrówka'))
armata = np.array(list('armata'))
armata = np.flip(armata)

wykreslanka = np.zeros((6,6), dtype='str')

print(wykreslanka)

wykreslanka = np.diag(mrowka)
wykreslanka[:, 0] = malina
#wykreslanka[5,::-1] = armata
wykreslanka[5,:] = armata
print(wykreslanka)
print("")
wykreslanka[:, 0] = mrowka
wykreslanka[5,::-1] = armata
for a in range(5):
    wykreslanka[a,a] = malina[a]
print(wykreslanka)

# zad7
def macierz(n):
    mac = np.zeros((n, n), dtype='int32')
    mac += np.diag([2 for _ in range(n)])
    for i in range(1, n):
        mac += np.diag([2+(2*i) for _ in range(n-i)], k=i)
        mac += np.diag([2+(2*i) for _ in range(n-i)], k=-i)
    print(mac)

macierz(3)

# zad8
def podziel(tab, kierunek='poziomo'):
    print(tab)
    if kierunek == 'poziomo':
        # nieparzysta liczba wierszy
        if tab.shape[0] % 2 != 0:
            print("Tablica posiada nieprzystą liczbę wierszy")
            return
        p1 = tab[0:int(tab.shape[0]/2), :]
        p2 = tab[int(tab.shape[0]/2):, :]
        print("***** część 1 *****")
        print(p1)
        print("***** część 2 *****")
        print(p2)
    elif kierunek == "pionowo":
        if tab.shape[1] % 2 != 0:
            print("Tablica posiada nieprzystą liczbę kolumn")
            return
        p1 = tab[:, 0:int(tab.shape[1]/2)]
        p2 = tab[:, int(tab.shape[1] / 2):]
        print("***** część 1 *****")
        print(p1)
        print("***** część 2 *****")
        print(p2)


podziel(np.arange(36).reshape((6,6)), kierunek='pionowo')

# zad9
def n_ty_wyraz(a1, n, r):
    return a1 + (n-1)*r


macierz = np.ones(25, dtype='int32')
print(macierz)
for a in range(0, 25, 1):
    element = n_ty_wyraz(4, a+1, 4)
    macierz[a] = element

macierz = macierz.reshape((5, 5))
print(macierz)





#-------------------    LAB 7   -------------------


import numpy as np

# Zad1
a = np.array([3, 4, 5])
b = np.array([6, 2, 4])
c = a * b
print(c)

# Zad2
a = np.array([[3, 7, 5], [6, 1, 9], [2, 7, 8]])
b = np.array([[5, 1, 6, 8], [3, 6, 2, 7], [9, 3, 7, 5], [4, 4, 2, 1]])
print(a)
print(b)

print(a.min(axis=0))
print(a.min(axis=1))
print(b.min(axis=0))
print(a.min(axis=1))

# Zad3
a = np.array([3, 4, 5])
b = np.array([6, 2, 4])
c = np.dot(a, b)
print(c)

# Zad4
a = np.array([3, 4, 5])
b = np.linspace(3, 10, 3)
c = a * b
print(c)

# Zad5,6,7
c = np.array([[60, 31], [45, 78], [15, 50]])
a = np.sin(c)
print(a)


d = np.array([[47, 24], [64, 28], [19, 33]])
b = np.cos(d)
print(b)
print("")
dodawanie = np.add(a,b)
print(dodawanie)

# Zad8
a = np.array([[3, 7, 5], [6, 1, 9], [2, 7, 8]])
for b in a:
    print(b)
    print("")

# Zad9
a = np.array([[3, 7, 5], [6, 1, 9], [2, 7, 8]])
for b in a.flat:
    print(b)
    print("")

#Zad10
macierz = np.arange(0,81,1).reshape(9,9)
print(macierz)

macierz_1 = macierz.reshape(3,27)
print(macierz_1)
macierz_2 = macierz.reshape(27,3)
print(macierz_2)
macierz_3 = macierz.reshape(81,1)
print(macierz_3)
macierz_4 = macierz.ravel()
print(macierz_4)

#Zad11
a = np.array([3, 7, 5, 6, 1, 9, 2, 7, 8, 6, 3, 6])
print(a)
macierz_1 = a.reshape(3, 4)
print(macierz_1)
print(macierz_1.ravel())
macierz_2 = macierz_1.reshape(4,3)
print(macierz_2)
print(macierz_2.ravel())
macierz_3 = macierz_1.reshape(2,6)
print(macierz_3)
print(macierz_3.ravel())






#-------------------    LAB 8   -------------------


import numpy as np
import pandas as pd

#zad1,2
plik = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(plik, header=0)

print(df[df.Liczba > 1000])
print('')
print(df[df.Imie == 'RADOSŁAW'])
print('')
print(df.Liczba.sum())
print('')
grupa = df[df.Rok < 2006]
print(grupa.Liczba.sum())
grupa = df[df.Rok < 2006].groupby('Rok').agg({'Liczba': ['sum']})
print(grupa)
print('')

print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).nth(0))
print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).first())

new_df = df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'])
for index, group in enumerate(new_df, start=1):
    print(f"{index} {group[0]}")
    print(f" {group[1].iloc[0]['Imie']}", end='')
    print(f" {group[1].iloc[0]['Liczba']}")
print('')
print("Chłopiec")
print(df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
                                                                                   ascending=False).iloc[0])
print("Dziewczynka")
print(df[df['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
                                                                           ascending=False).iloc[0])

#zad3

df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')

print(df['Sprzedawca'].unique())
print('')
print(df.sort_values('Utarg', ascending=False).head(5))
print('')
print(df.groupby('Sprzedawca').size())
print('')
print(df.groupby('Kraj').agg({'Utarg': ['sum']}))
print(df.groupby('Kraj').size())
print('')
print(df[(df['Kraj'] == 'Polska') & (df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31')].
      agg({'Utarg': ['sum']}))
print('')
print(df[df['Data zamowienia'].str[:4] == '2004'].agg({'Utarg': ['mean']}))
rok_2004 = df[((df[ 'Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31'))]
rok_2004.to_csv("zamowienia_2004.csv", index=False)




#-------------------    LAB 9   -------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)
# zad1
roczniki = df['Rok'].unique()
grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
wykres = grupa.plot()
wykres.set_ylabel('Liczba urodzonych dzieci')
wykres.set_xticks(roczniki)
wykres.tick_params(axis='x', labelrotation=40)
wykres.legend()
plt.subplots_adjust(left=0.15, right=0.9, bottom=0.15, top=0.9)
plt.title("Liczba urodzonych dzieci dla każdego roku")
plt.show()
#zad2
grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
wykres = grupa.plot.bar(ylabel='Liczba urodzeń')
wykres.legend()
plt.xticks(rotation=0)
plt.title("Liczba urodzonych chłopców i dziewczynek")
plt.show()
#zad3
grupa = df[df['Rok'] > 2012].groupby(['Plec']).agg({'Liczba':['sum']})
wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20)
plt.legend()
plt.show()
#zad4
df = pd.read_csv('zamowienia.csv', delimiter=';')
policzone = df.groupby('Sprzedawca').size()
policzone.plot.bar()
plt.ylabel("liczba zamówień")
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.2, top=0.9)
plt.title('Ilość zamówień sprzedawców')
plt.show()





#-------------------    LAB 10   -------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



#zad1
# x = np.arange(1, 21, 1)
# plt.plot(x, 1/x, label='f(x) = 1/x')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.axis([0, 20, 0, 1])
# plt.legend()
# plt.title('Wykres funkcji f(x) = 1/x dla x[1,20]')
# plt.show()
# zad2
# x = np.arange(1, 21, 1)
# plt.plot(x, 1/x, 'g>:', label='f(x) = 1/x' )
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.axis([0, 20, 0, 1])
# plt.legend()
# plt.title('Wykres funkcji f(x) = 1/x dla x[1,20]')
# plt.show()
# zad3
# x = np.arange(0, 30, .1)
# plt.plot(x, np.sin(x), 'b', label='sin(x)')
# plt.plot(x, np.cos(x), 'r', label='cos(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x) cos(x)')
# plt.legend(loc='upper right')
# plt.title('Wykres sin(x), cos(x)')
# plt.show()

# zad4
# df = pd.read_csv('iris.data', header=0, sep=',', decimal='.')
# print(df)
# # przygotowanie wektora kolorów
# colors = np.random.randint(0, 50, len(df.index))
# # przygotowanie wektora z rozmiarami 'kropek'
# scale = np.abs(df['sepal length'] - df['sepal width'])
#
#
# plt.scatter(df['sepal length'], df['sepal width'], c=colors, s=scale)
# plt.xlabel('sepal length')
# plt.ylabel('sepal width')
# plt.show()
#zad5
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)
# plt.subplot(1, 3, 1)
# grouped = df.groupby('Plec')
# etykiety = list(grouped.groups.keys())
# wartosci = list(grouped.agg('Liczba').sum())
# plt.bar(x=etykiety, height=wartosci, color=['green', 'red'])
# plt.xlabel('Płeć')
# plt.ylabel('Liczba narodzonych dzieci')
# # wykres 2
# plt.subplot(1, 3, 2)
# x = df['Rok'].unique()
# kobiety = df[(df.Plec == 'K')].groupby('Rok').agg({'Liczba':['sum']}).values
# mezczyzni = df[(df.Plec == 'M')].groupby('Rok').agg({'Liczba':['sum']}).values
# plt.plot(x, kobiety, label="Kobiety")
# plt.plot(x, mezczyzni, label="Mężczyźni")
# plt.xlabel('Rok')
# #
# # # wykres 3
# plt.subplot(1, 3, 3)
# x = df['Rok'].unique()
# y = df.groupby('Rok').agg('Liczba').sum()
# plt.bar(x, y)
# plt.xlabel('Rok')
# # wyświetlamy cały wykres
# plt.subplots_adjust(wspace=0.85)
# plt.show()
#zad6
df = pd.read_csv('zamowienia.csv', sep=';')
policzone = df.groupby('Sprzedawca')['Utarg'].sum()
print(policzone)
# explode
explode = [0.0 for n in range(len(policzone.index))]
# określamy które kawałki i o ile wysunąć, tu losujemy jeden
explode[np.random.randint(0, len(policzone.index))] = 0.2
wedges, texts, autotext = plt.pie(x=policzone, labels=policzone.index,
                                  autopct=lambda pct: "{:.2f}%".format(pct), textprops=dict(color='black'), explode=explode, shadow=True)
plt.title("Procentowy udział kwot zamówień sprzedawców")
plt.show()