import os
os.system("cls")

k1= float(input("digite sua idade:"))

if k1 < 16:
    print("!!nao pode votar!!")

elif k1 <= 17:
    print("voto opisional")

elif k1 >= 65:
    print("!! voto nao e obrigatorio!!")        

else :
   print("e obrigado a votar")