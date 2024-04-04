a=int(input("entrer 1ere nombre : "))
b=int(input("entrer 2eme nombre : "))
operateur=input("entrer l'operateur : ")
if operateur == "+" :
    s=a+b
elif operateur == "-" :
    s=a-b
elif operateur == "*" :
    s=a*b
else :
    s=a/b
print("resultat :",s)