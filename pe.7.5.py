def gemiddelde():
    zin = input(str('geef een zin op'))
    lengtezin= len(zin)
    aantalniks = zin.count(' ')
    aantalwoorden = aantalniks + 1
    gemiddeldewoorden = (lengtezin- aantalniks )/ (aantalwoorden)

    print (gemiddeldewoorden)

gemiddelde()