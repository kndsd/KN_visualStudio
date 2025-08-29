import os
os.system("cls")



login= str("kuezin085")
senha= str("3386")

l = str(input("login:"))
s = str( input("senha:"))

if l == login and s == senha:
    print("bem vindo ")

elif l == login and s != senha:
    print("senha invalida ")

elif l != login and s == senha:
    print("login invalido")    

else:
    print("login e senha invalida")    