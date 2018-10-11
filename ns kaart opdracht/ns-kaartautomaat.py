stations=['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
def inlezen_beginstation(stations1):
    while True:
        beginstationf= input('wat is je begin station')
        if beginstationf in stations1:
            print('deze locatie is correct')
            break
        else:
            print('doe het opnieuw')
    return beginstationf


def inlezen_eindstation(stations2, beginstationf):
    while True:
        eindstationf= input('wat is je eindstation')
        if eindstationf in stations2:
            index1=stations.index(eindstationf)
            index2=stations.index(beginstationf)
            if index1 <= index2:
                print('dit is incorrect. het eindstation is eerder dan het beginstation')
            else:
                print('dit is correct')
                break
        else: print('incorrecte eindlocatie')
    return eindstationf
def omroepen_reis(stations3, beginstationf, eindstationf):
    index1= stations3.index(beginstationf)
    index2 = stations3.index(eindstationf)
    aantals=stations3.index(eindstationf)-stations3.index(beginstationf)
    prijs= aantals * 5
    print('het beginstation is',beginstationf, 'dit is het',index1,'traject')
    print('het eindstation is', eindstationf, 'dit is het', index2, 'traject')
    print('de afstand is',aantals,'station(s)')
    print('de prijs van de kaarts is',prijs,'euro')
    print('je stapt in de trein:',beginstationf)
    for i in range(index1+1, index2):
        if i is not '':
            print('-',stations3[i])
    print('je stapt uit bij:',eindstationf)
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
