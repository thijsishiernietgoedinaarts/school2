
#naam= input('naam')
#eind= input('eind')
#begin= input('begin')
#totaal= naam+eind+begin
def code(invoerstring):
    newantwoord = ''
    for x in invoerstring:
        x2= ord(x)
        x3=int(x2) + 3
        x4=chr(int(x3))
        newantwoord= newantwoord + x4
    print(newantwoord)

code("RutteAlkmaarDen Helder")
