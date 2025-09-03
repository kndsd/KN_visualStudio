import os
os.system("cls")
print ("valor do produto")
print("""
forma\t\t\tcodigo\t\t\tcodicão
avista\t\t\t1\t\t\t10% de sescomto 
parselado\t\t2\t\t\tvalor dividido ate 6             

""")
forma = int (input("dijite a forma do pagamento:"))
v= 100

if forma == 1:
    av = v - (v*0.1)
    print (f"valor final :{av}")
    

elif forma == 2:
     dv = v / 6
     print(f"6 parselas de {dv}")  

else: 
 print ("!!!!!!!opisao invalida!!!!!!!!!")  

 