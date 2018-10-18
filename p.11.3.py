import csv

with open('game.csv' ,'r') as mycsvfile:
    reader = csv.reader(mycsvfile, delimiter=';')
    newlst=[]
    for row in reader:
        grootste= 0
        scorelijst=  ('gamer: {}, datum: {}, score:{}'.format(row[0], row[1], row[2]))
        print(scorelijst)
        newlst.append(scorelijst)
        if int(row[2]) >= grootste:
            grootste = row[2]


with open('game.csv', 'r') as mycsvfile:
    reader = csv.reader(mycsvfile, delimiter=';')

    for row in reader:


        if row[2] == str(grootste):
            print(row[0], 'heeft de hoogste score met', row[2], 'gehaald op', row[1])

