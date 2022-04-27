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


