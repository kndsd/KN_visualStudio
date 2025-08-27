import os
os.system("cls")

peso =  int(input("escreva o seu peso:"))
altura = float(input("escreva sua altura:"))

imc = peso/(altura*altura)

if imc < 18.5 :
    print("!!peso baixo!!") 

elif imc <= 18.5:    
    print("peso normal")

    