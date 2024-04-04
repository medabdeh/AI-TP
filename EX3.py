t=int(input("entrer  temps en secondes : "))
def convertir(t):
    return str(int(t/3600))+" heures "+str(int((t%3600)/60))+" minutes "+str(((t%3600)%60))
print(convertir(t))