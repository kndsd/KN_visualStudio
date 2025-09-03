import os
os.system("cls")

print("""

codigo \t\t\t prato \t\t\t preço
      1\t\t\t pizza \t\t\t 10.50$
      2\t\t\t strogonoff\t\t\t 30.00$
      3\t\t\t frago assado\t\t 50.00$
      4\t\t\t pamonha\t\t\t 14.00$
      5\t\t\t cu de wesley\t\t 00.00$

""")
k1= int(input("escolha a opisao no meno"))
match k1:
      case 1: 

            print("pizza 10.50$")

      case 2 :
  
            print("strogonoff 30,00$")

      case 3 :
   
            print("frago assado 50.00$")

      case 4 :

       print("pamonha 14.00$")

      case 5:
   
            print("cu de wesley 00.00$")