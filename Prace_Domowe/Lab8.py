import math
import pandas as pd
import numpy as np

#Zadanie 1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
#print(df.to_string())
#print(df)
print('======================================================')
print()

#Zadanie 2
# print(df.where(df.Liczba > 1000)) # & df.groupby(df.Rok))   #TypeError: '>' not supported between instances of 'list' and 'int'
# liczba = ( df.loc[df['Liczba'] > 1000] & df.groupby(['Rok']))
liczba = df.loc[df['Liczba'] > 1000]
print(liczba)
print('======================================================')
print()

imie = df.loc[df['Imie'] == 'BOGUMIŁ']
print(imie)
print('======================================================')
print()

print(df.groupby(['Rok']).agg({'Liczba':['sum']}))
print('======================================================')
print()

suma05 = df[df["Rok"] <= 2005].groupby(["Rok"])
print(suma05.agg({"Liczba" : ["sum"]}))
print('======================================================')
print()

suma_plec = df.groupby(["Plec"])
print(suma_plec.agg({"Liczba" : ["sum"]}))
print('======================================================')
print()

najpopularniejsze = df.loc[df.groupby(["Rok", "Plec"])["Liczba"].idxmax()]
print(najpopularniejsze)
print('======================================================')
print()

najpopularniejsze2 = df.loc[df.groupby(["Plec"])["Liczba"].idxmax()]
print(najpopularniejsze2)
print('======================================================')
print()

#Zadanie 3
df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
print()
print(df)
print('======================================================')
print()

print( pd.unique(df.Sprzedawca) )
print('======================================================')
print()

print( df['Utarg'].nlargest(n=5) )
print('======================================================')
print()

ilosc = df.groupby(["Sprzedawca"])
print(ilosc.agg({"Utarg" : ["sum"]}))   #suma wartosci zamowien
print()
print(df['Sprzedawca'].value_counts(ascending=False))     #suma ilosci zamowien
print('======================================================')
print()

ilosc = df.groupby(["Kraj"])
print(ilosc.agg({"Utarg" : ["sum"]}))   #suma wartosci zamowien
print()
print(df['Kraj'].value_counts(ascending=False))     #suma ilosci zamowien
print('======================================================')
print()

print(df['Kraj'].value_counts(ascending=False))
print('======================================================')
print()
