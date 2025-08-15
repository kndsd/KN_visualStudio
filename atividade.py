#atv 1 kaue

import os
os.system("cls")

print("ola usuario, me indique 2 numeros a serem operados")

p1 = float(input("digite o primeiro numero:"))
p2 = float(input("digite o segundo  numero:"))

p3 = p1 + p2
p4 = p1 * p2 
p5 = p1 - p2
p6 = p1 / p2

print (f"soma:{p3}")
print (f"mutiplicacao:{p4}")
print (f"subtração:{p5}")
print (f"divisao:{p6}")