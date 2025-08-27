import os
os.system("cls")


nome = input ("escreva seu nome:")

nota1=float(input("escreva a nota") )
nota2=float(input("escreva a nota") )
nota3=float(input("escreva a nota") )

media= (nota1 + nota2 + nota3 ) / 3
print ("funsianamento:")
print("A = aprovado")
print("B = aprovado")
print("C = aprovado ")
print("D = reprovado")
print("E = reprovado")
if media >= 9:
     print("A")
     print("aprovado")

elif media >= 7.5:

      print("B") 
      print("aprovado")    

elif media < 7.5:
     print("C")

elif media >= 4:
       print("D")
       print("reprovado")


else:
   print ("e")    
   print("reprovado")
