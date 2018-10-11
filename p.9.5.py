dic={}
newgetal=0
lijst=[]

while True:
    naam=(input('geef een naam op'))
    if naam=='':
        break
    lijst.append(naam)
for f in lijst:
    dic[f]=lijst.count(f)

print(dic)