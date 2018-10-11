def standaardprijs(afstandKM):
    if afstandKM <= 0:
        return 0.0
    if afstandKM >= 50:
        prijs = 15 + 0.60*afstandKM
        return prijs
    else:
        prijs= 0.80 * afstandKM
        return prijs


def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs= standaardprijs(afstandKM)
    if leeftijd < 12 or leeftijd > 64:
        if weekendrit:
            nettoprijs= prijs * 0.65
            return nettoprijs
        else:
            nettoprijs = prijs * 0.70
            return nettoprijs
    else:
        if weekendrit:
           nettoprijs = prijs * 0.60
           return nettoprijs
        else:
            nettoprijs = prijs
            return nettoprijs

print(ritprijs(11, False, 30))
print(ritprijs(12, False, 30))
print(ritprijs(64, False, 30))
print(ritprijs(65, False, 30))
print(ritprijs(11, True, 30))
print(ritprijs(12, True, 30))
print(ritprijs(64, True, 30))
print(ritprijs(65, True, 30))
print(ritprijs(11, False, 80))
print(ritprijs(12, False, 80))
print(ritprijs(64, False, 80))
print(ritprijs(65, False, 80))
print(ritprijs(11, True, 80))
print(ritprijs(12, True, 80))
print(ritprijs(64, True, 80))
print(ritprijs(65, True, 80))
print(ritprijs(11, False, -10))
print(ritprijs(12, False, -10))
print(ritprijs(64, False, -10))
print(ritprijs(65, False, -10))
print(ritprijs(11, True, -10))
print(ritprijs(12, True, -10))
print(ritprijs(64, True, -10))
print(ritprijs(65, True, -10))



afstandKM= float(input('hoe ver ga je reizen'))
if afstandKM < 0:
    afstandKM= 0
    print(afstandKM)
opleeftijd = float(input('hoe oud ben je '))
opweekendrit= eval(input('is het het weekend'))
print(opweekendrit)
totaalprijs= standaardprijs(afstandKM)
print('de totaal prijs is  €', totaalprijs)

totaal=ritprijs(opleeftijd, opweekendrit, afstandKM)
print('met de korting is de prijs  €', totaal)
