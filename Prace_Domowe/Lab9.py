import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
# print(ts)
# ts.plot()
# plt.savefig('wykres.png')   #zeby zapisac .jpg trzeba uzyc biblioteki pillow - na egzamin
# plt.show()
#
# dane = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Dehli', 'Brasilia', 'Warszawa'],
#         'Populacja' : [11000000, 1300000000, 220000000, 36000000],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']}
#
# df = pd.DataFrame(dane)
# grupa = df.groupby('Kontynent').agg({'Populacja': ['sum']})
#
# grupa.plot(kind='bar', ylabel='Populacja w mld', xlabel='Kontynent',
#            rot=0, legend=True, title='Populacja dla kontynentow', color='magenta')
# plt.legend(loc='upper left')
# plt.show()
#
#
# df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df)
#
# grupa = df.groupby('Imię i nazwisko').agg({'Wartość zamówienia': ['sum']})
# grupa.plot(kind='pie', subplots=True, autopct='%.2f %%',
#            fontsize=20, figsize=(6, 6))
# plt.legend(loc='upper left')
# plt.show()
#
#
# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
# df = pd.DataFrame(ts)
# print(df)
# df['Średnia krocząca'] = df.rolling(window=50).mean()
# print(df)
# df.plot()
# plt.legend(['Wartości', 'Średnia krocząca'])
# plt.show()



#Zadania z pliku 'pandas wykresy zadania.docx'
xlsx = pd.ExcelFile('imiona.xlsx')      #biblioteka openpyxl
df = pd.read_excel(xlsx, header=0)

# #Zadanie 1 - Stwórz wykres liniowy, który wyświetli liczbę urodzonych dzieci dla każdego roku.
# df = pd.DataFrame(df)
# grupa = df.groupby('Rok').agg({'Liczba': ['sum']})
# # lista=df['Rok'].uniqe()
# # xticks = lista
# grupa.plot(kind='line', ylabel='Liczba urodzonych', xlabel='Rok',
#            rot=0, legend=True, title='Liczba urodzonych dzieci dla każdego roku', color='magenta')
# plt.legend(loc='upper left')
# plt.show()

# #Zadanie 2 - Stwórz wykres słupkowy, który wyświetli liczbę urodzonych chłopców i dziewczynek z całego zbioru.
# df = pd.DataFrame(df)
# grupa = df.groupby('Plec').agg({'Liczba': ['sum']})
# grupa.plot(kind='bar', ylabel='Liczba urodzonych', xlabel='Płeć',
#            rot=0, legend=True, title='Liczba urodzonych chłopców i dziewczynek', color='blue')
# plt.legend(loc='upper left')
# plt.show()      #jak zamienic 10^6 * ilosc na zwykly zapis?

# #Zadanie 3 - Wykres kołowy z waściartomi % ukazującymi ilość urodzonych chłopców i dziewczynek w ostatnich 5 latach z datasetu.
# grupa = df.groupby('Plec').agg({'Liczba': ['sum']})   #Jak to połączyć z zakresem lat ?
#
# # print(df.loc["2012":"2017"])
# # lata = pd.date_range(start='1/1/2012', end='2017/12/31')
# # print(lata)
#
# grupa.plot(kind='pie', subplots=True, autopct='%.2f %%',
#            fontsize=20, figsize=(6, 6))
# plt.legend(loc='upper left')
# plt.show()

# # Zadanie 4 - Wyświetl na pomocą wykresu słupkowego ilość złożonych zamówień przez poszczególnych sprzedawców (zbiór danych zamówienia.csv).
# df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
# df = pd.DataFrame(df)
#
# ilosc_zamowien = df['Sprzedawca'].value_counts()
# print(ilosc_zamowien)
# grupa = ilosc_zamowien
# grupa.plot(kind='bar', ylabel='Liczba złożonych zamówien', xlabel='Sprzedawca',
#            rot=0, legend=True, title='ilość złożonych zamówień przez poszczególnych sprzedawców', color='blue')
#
# plt.legend(loc='upper right')
# plt.show()
