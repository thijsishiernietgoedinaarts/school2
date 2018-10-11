loop=0
newgetal=0
lijst=11
while lijst >10:
    getal=int(input('geef een getal op'))
    newgetal= newgetal+getal
    loop +=1
    if getal == 0:
        loop= loop -1
        break
print('er zijn',loop, 'getallen ingevoerd')
print('klaar',newgetal)