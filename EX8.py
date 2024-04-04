n=int(input("entrer le nombre de depart : "))
s="s="
S=0
for i in range(n):
    S=S+10**i
    s=s+str(10**i)+"+"
s=s+str(10**n)
S=S+10**n
print(s+"=",S)