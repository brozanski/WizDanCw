import sys
import math
import random
# #Zad. 1
# a = []
# for x in range(1,11):
#     a.append(1-x)
# print(a)
#
# b = []
# for y in range(8):
#     b.append(4**y)
# print(b)
#
# c = []
# for z in b:
#     if z % 2 == 0:
#         c.append(z)
# print(c)

# #Zad. 2
# lista1 = []
# i=1
# while i<11:
#     x = (random.randint(0, 30))
#     lista1.append(x)
#     i+=1
# print(lista1)
#
# lista2 = []
# for y in lista1:
#     if y % 2 == 0:
#         lista2.append(y)
# print(lista2)

# # #Zad. 3
# slownik = {'szt.' : ["Mango", "Pączek", "Bluza"],
#            'litr' : ["Pepsi","Olej"],
#            'kg' : ["Mąka","Banany"]}
# # print(slownik)
# # sztuki = []
# # for key in slownik.items():
# #     if key == 'szt.'
# #         sztuki.append(values)
# sztuki =  [slownik[x] for x in slownik.keys() if x=='szt.']
# print(sztuki)

# #Zad. 4
# def trojkat_prostokatny(a,b,c):
#     wzor = (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2)
#
#     if wzor:
#         print("Trojkąt jest prostokątny!")
#         return 1
#     else:
#         print("Trojkąt nie jest prostokątny!")
#         return 0
# print(trojkat_prostokatny(3,4,5))
# print(trojkat_prostokatny(5,4,3))
# print(trojkat_prostokatny(4,6,8))

# #Zad. 5
# def pole_trapezu (a,b,h):
#     pole = ((a+b)*h)/2
#     return pole
# print(pole_trapezu(4,6,8))

# #Zad. 6
# def iloczyn(a=1,b=4,ile=10):
#   for i in range (ile):
#     a*=b
#   return a
# print(iloczyn())
