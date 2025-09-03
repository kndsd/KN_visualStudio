import os
os.system("cls")
so= int(input("digite 1 se for homen se for mulher 2:"))
al= float(input("dijite sua altura:"))


if so == 1 :
    cm = (72.7*al)-58

elif so == 2 :
    cm = (62.1 * al)-44.7

else:
    print("!!!!sexo nao encomtrado!!!!!")

print(f"pesso ideal:{cm} ")
