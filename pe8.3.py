invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
def gemiddel(x):
    y = x.split('-')
    newy= []
    for f in y:
        g = int(f)
        newy.append(g)
    newy.sort()
    sumy = sum(newy)
    print(len(newy))
    mxy=max(newy)
    miny=min(newy)
    lent= len(newy)
    avery= sumy / lent
    print('Gesorteerde list van ints:', newy, '\n' 'Grootste getal:',mxy, 'en Kleinstegetal:', miny, '\n' 'Aantal getallen: ',lent, 'en Som van de getallen:', sumy, '\n' 
'Gemiddelde:', avery)
gemiddel(invoer)
