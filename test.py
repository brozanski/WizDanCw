import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns

#Zadanie 1
df = pd.read_csv('flag.csv', header=0, sep=',',decimal='.')
print(df)

df = pd.DataFrame(df)
df1 = df.tail(75)
religia = df.groupby('religion').agg({'population': ['sum']})

religia.plot(kind='bar', ylabel='Populacja', xlabel='Religia',
           rot=0, legend=True, title='Liczebność danego wyzwania')
plt.legend(loc='upper left')
plt.show()
plt.savefig("Religia.png")


#Zadanie 2 - brak pliku png

#Zadanie 3      - Europa ma numer 3
df = pd.read_csv('flag.csv', header=0, sep=',',decimal='.')
df = pd.DataFrame(df)

# grupa = df[(df['landmass'] == 3) & (df['religion'])].agg({'population': ['sum']})
grupa = df[(df.landmass == 3)].groupby('religion').agg({'population':['sum']})
grupa.plot(kind='pie', subplots=True, title='Wykres kolowy - procentowy udzial religii w Europie', autopct='%.2f %%',
           fontsize=14, figsize=(6, 6), legend=True)

# pd.set_option('display.max_columns', None)
a = (df[df.landmass == 3])
print(a)

# plik = open("europa.csv", 'w+', encoding='utf-8')
# a = (df[df.landmass == 3])
# plik.write(str(a))
# plik.close

plt.show()


Zadanie 4  - seaborn, wykres punktowy
df = pd.read_csv('flag.csv', header=0, sep=',',decimal='.')
df = pd.DataFrame(df)
df = df.tail(75)
df = df['area']

data ={'a': df,
    'b': np.random.randint(25, 200, 75)}

plot = sns.relplot(data=df, x='a', y='b',palette='muted', legend=True, title="Wykres")
plt.show()

sns.set()
