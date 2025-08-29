import os
os.system("cls")

peso =  int(input("escreva o seu peso:"))
altura = float(input("escreva sua altura:"))

imc = peso/(altura*altura)

if imc < 18.5 :
    print("!!peso baixo!!") 

elif 18.6 <= imc <= 24.9:    
    print("peso normal")

elif  25.0 <= imc <= 29.9:
    print("peso levimente asima")

elif 30.0 <= imc <= 34.9:
      print ("obesidade 1")

elif 35.0 <= imc <= 39.9:
     print("obesidade 2") 

else: 
  print("obesidade 3")

    
