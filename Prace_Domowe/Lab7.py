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
