import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#       ZESTAW 41

# Zad.1. Na jednym wykresie narysuj wykresy krzywych: y = log(2x), y = −4x + 2, y = 2 cos(x) na przedziale
# [0.5, 10]. Wykres powinien posiadać tytuł, legendę, podpisane etykiety obu osi. Dodaj siatkę na wykres.
# Linie krzywych powinny mieć różne style i różne kolory inne niż domyślne. Zapisz wykres w formacie png za
# pomocą kodu

x=np.linspace(0.5,10,100)
y1=np.log2(x)
y2=-4*x+2
y3=2*np.cos(x)

fig, axs = plt.subplots()
axs.set_ylim([-3, 3])
axs.plot(x, y1, ls='--' ,label='log(2x)', color = "green")
axs.plot(x, y2,ls='dotted', label='-4x+2', color = "red")
axs.plot(x, y3,ls='-.', label='2cos(x)', color = "blue")
axs.set_xlabel("oś pozioma")
axs.set_ylabel("oś pionowa po lewej stronie")
plt.title("Wykresy - kilka")
plt.legend()
plt.grid()
plt.savefig("Zadanie1")
plt.show()



# Zad.2. W jednym pliku wykonaj poniższe czynności:
#   załaduj dane z pliku ceny41.xlsx jako ramkę danych (Data Frame),
df=pd.read_excel("ceny41.xlsx")

#   wyświetl na konsoli średnią cenę poszczególnych produktów ze wszystkich miesięcy
c = df.loc[df["Rodzaje towarów i usług"]== "cebula - za 1 kg"]
m = df.loc[df["Rodzaje towarów i usług"]== "marchew - za 1 kg"]
z = df.loc[df["Rodzaje towarów i usług"]== "ziemniaki - za 1 kg"]

cenac  = c["Wartosc"]
miesiacc = c["Miesiące"]
cenam  = m["Wartosc"]
miesiacm = m["Miesiące"]
cenaz  = z["Wartosc"]
miesiacz = z["Miesiące"]

print("Cebula za 1 kg : ", c["Wartosc"].mean())
print("Marchew za 1 kg : ", m["Wartosc"].mean())
print("Ziemniaki za 1 kg : ", z["Wartosc"].mean())

# stwórz wykres liniowy prezentujący dane zawarte w ramce danych (wszystkie dane)
#   umieść swój numer indeksu w lewym dolnym rogu wykresu.

fig, axs = plt.subplots(figsize=(15,5))
axs.plot(miesiacm, cenam, ls='--' ,label='Marchew', color = "orange")
axs.plot(miesiacc, cenac, ls='-.' ,label='Cebula', color = "gold")
axs.plot(miesiacz, cenaz, ls='dotted' ,label='Ziemniaki', color = "brown")
axs.set_xlabel("Miesiące")
axs.set_ylabel("Ceny w zł")
# plt.text(0,1, "166311")
plt.annotate(xy=[-0.3, 1.1], text="166311")
plt.grid()
plt.legend()
plt.title("Cena towaru za 1 kg rok 2017")
plt.savefig("zadanie2.jpg")
plt.show()



# Zad.3. W jednym pliku wykonaj poniższe czynności:
# • załaduj dane z pliku cechy41.csv,
dane = pd.read_csv("cechy41.csv", decimal=',', sep=';')

# • podziel wartości obu cech na koszyki od 0 do 200 z krokiem 50
cecha1 = dane["Cecha1"]
cecha2 = dane["Cecha2"]
cat = [0, 50, 100, 150, 200]

p1 = pd.cut(cecha1, bins=cat)
koszyk1 = pd.value_counts(p1, sort=False)
p2 = pd.cut(cecha2, cat)
koszyk2 = pd.value_counts(p2, sort=False)

# • stwórz wykres słupkowy poziomy prezentujący dane zawarte w pliku (mogą być dwa wykresy)
# • Wykres powinien być estetyczny i podpisany. Im więcej - tym lepiej.
x = np.arange(4)
plt.subplot(2, 1, 1)
plt.barh(x, koszyk1, alpha=0.75, color="green")
plt.title("Cecha 1")
plt.grid()

plt.subplot(2, 1, 2)
plt.barh(x, koszyk2, alpha=0.75, color="purple")
plt.title("Cecha 2")
plt.grid()

plt.tight_layout()
plt.savefig("Zadanie3.jpg")
plt.show()

