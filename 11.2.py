import datetime
import csv
while True:
    print('nieuw bestand')
    cool= 0
    with open('inloggers.csv', 'a', newline='') as mycsvfile:
        writer =csv.writer(mycsvfile, delimiter=';')

        while cool==0:
            naam = input("Wat is je achternaam? ")
            if naam == '':
                cool = 1
                continue
            voorl = input("Wat zijn je voorletters? ")
            gbdatum = input("Wat is je geboortedatum? ")
            email = input("Wat is je e-mail adres? ")
            vandaag = datetime.datetime.today()
            s = vandaag.strftime("%a %d %b %Y at %H:%M:%S")
            antwoord=[s,voorl,naam,gbdatum,email]
            if cool == 0:
                writer.writerow((s,voorl,naam,gbdatum,email,))
            #wanneer de volgende persoon inlogt is onbekend, dus schrijf meteen naar file
