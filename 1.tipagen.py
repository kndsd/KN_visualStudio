
import os
os.system("cls")

k1=float(input("escreva um numero:"))
         
k2=float(input("segundo numero:"))

k3= (k1 + k2)

k4= (k3 / 2)

k5=(k1*k2)

if  k1 > k2:
   print(f"  {k1}   maior que {k2} " )

elif  k1 < k2:
     print(f"{k1} menor que {k2}")
     
elif k1 == k2:
    print("!!!!numerus iguais!!!!")


     
print(f"media:{k4}")
print(f"produto:{k5}")
print(f"soma:{k3}")