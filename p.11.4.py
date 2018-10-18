import decimal
import csv
headers= ['Artikelnummer','Artikelcode','Naam','Voorraad','Prijs']
with open('header.csv', 'w', newline='') as mycsvfile:
    writer = csv.writer(mycsvfile, delimiter=';')
    writer.writerow(('Artikelnummer','Artikelcode','Naam','Voorraad','Prijs'))
    writer.writerow(('121', 'ABC123','Highlight pen','231',0.56))
    writer.writerow(('123', 'PQR678', 'Nietmachine', '587', 9.99))
    writer.writerow(('128', 'ZYX163', 'Bureaulamp', '34', 19.95))
    writer.writerow(('137', 'MLK709', 'Monitorstandaard', '66', 32.50))
    writer.writerow(('271', 'TRS665', 'Ipad hoes', '155', 19.01))

with open('header.csv' ,'r') as mycsvfile:
    reader =csv.reader(mycsvfile, delimiter=';')
    grootste=0
    next(reader)
    for line in reader:
        getal= float(line[4])
        newgetal= getal
        if newgetal > grootste:
            grootste = newgetal

with open('header.csv' ,'r') as mycsvfile:
    print(grootste)
    reader =csv.reader(mycsvfile, delimiter=';')
    next(reader)
    for line in reader:
        newline= float(line[4])
        if str(grootste) == str(newline):
            print('het duurste artikel is',line[2],'en die kost',line[4],'Euro')

with open('header.csv' ,'r') as mycsvfile:
    reader =csv.reader(mycsvfile, delimiter=';')
    next(reader)
    kleinste=5000000
    for row in reader:
        if int(row[3])< kleinste:
            kleinste = int(row[3])

with open('header.csv' ,'r') as mycsvfile:
    reader =csv.reader(mycsvfile, delimiter=';')
    next(reader)
    for row in reader:
        if str(kleinste) == row[3]:
            print('er zijn slecht ',row[3],'exemplaren in de vooraad en het product heeft nummer',row[0])

with open('header.csv' ,'r') as mycsvfile:
    reader =csv.reader(mycsvfile, delimiter=';')
    next(reader)
    vooraad=0
    for row in reader:
        vooraad= vooraad + int(row[3])
    print('intotaal hebben wij',vooraad,'producten in ons magazijn liggen')