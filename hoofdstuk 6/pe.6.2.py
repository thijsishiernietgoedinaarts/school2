rphonebook = {'(123)456-78-90':['Anna','Karenina'],'(901)234-56-78':['Yu', 'Tsun'],'(321)908-76-54':['Hans', 'Castorp']}

def rlookup(x):
    num=str(input('geef een nummer'))
    print(x[num])
rlookup(rphonebook)