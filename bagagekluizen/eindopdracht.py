f='yes'
def kluis_openen():
    antwoord='niet'
    kluis= input('wat is je kluisnummer')
    pas= input('wat is je code')
    infile = open('C:/Users/jack/PycharmProjects/untitled/bagagekluizen/kluizen.txt', 'r+')
    content = infile.read()
    newcontent = content.split()
    paskluis= kluis+';'+pas
    for i in newcontent:
        if paskluis == i:
            antwoord='correct'
    if antwoord=='correct':
        print('je kluis is nu open')
    else:
        print('foute code')
def nieuwe_kluis():
    gevondenkluizen=[]
    lijst=[1,2,3,4,5,6,7,8,9,10,11,12]
    newlist=[]
    infile = open('C:/Users/jack/PycharmProjects/untitled/bagagekluizen/kluizen.txt', 'r+')
    content = infile.readlines()
    #loop door het bestand
     #   neem het kluisnr
      #  verwijder kluisnr uit lijst
    newcontent= content
    for regel in content:
        regel = regel.split(';')
        gevondenkluizen.append(int(regel[0]))
        lijst = [x for x in lijst if x not in gevondenkluizen]
    for x in lijst:
        if x not in gevondenkluizen:
            newlist.append(x)

    if len(content) <12:
        print('vrije kluizen',lijst)
        code=input('voer een code op')
        if len(code) >3:
            infile.write(str(min(newlist)) + ';'+str(code) + '\n')
            print('je kluisnummer is ' + str(min(newlist)) + ' je code is ' + code)

        else:
            print('fout code moet langer zijn dan 3 letters')
    else:
        print('er zijn geen kluizen meer vrij')
    infile.close()

def toon_aantal_kluizen_vrij():
    with open('kluizen.txt') as f:
        for i, l in enumerate(f):
            pass
    print(12-i-1)


while f=='yes':
    inp = int(input(
        '\n \n 1: Ik wil weten hoeveel kluizen nog vrij zijn \n2: Ik wil een nieuwe kluis  \n3: Ik wil even iets uit mijn kluis halen \n4: Ik geef mijn kluis terug'))
    if inp == 1:
        toon_aantal_kluizen_vrij()
    elif inp == 2:
        nieuwe_kluis()
    elif inp == 3:
        kluis_openen()
    elif inp == 4:
        kluis_teruggeven()