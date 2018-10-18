import requests
import xmltodict
def getstation():
    x= input('naar welk station wilt u\n1) utrecht\n2)denbosch\n3)eindhoven')
    if x == '1':
        return 'ut'
    if x == '2':
        return 'db'
    if x == '3':
        return 'eindhoven'

def getinformation(x): #dit haalt alle informatie
    auth_details = ('thijsaarts.aarts@student.hu.nl', '1IbHrkNUhwW6Bnezbn0C9F9_0GKMLSBkXo7vmFW97EHmfaMnVd2Oaw')
    api_url1 = 'http://webservices.ns.nl/ns-api-avt?station='
    api_url2='http://webservices.ns.nl/ns-api-avt?station=ut'
    api_urla = api_url1 + x
    response = requests.get(api_urla, auth=auth_details)
    with open('vertrektijden.xml', 'w') as myXMLFile:
        myXMLFile.write(response.text)
    vertrekXML = xmltodict.parse(response.text)


    #sortedvetreklijst(vertrekXML)
    lijst=[]
    grotelijst=[]

    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:

        eindbestemming = vertrek['EindBestemming']

        vertrektijd = vertrek['VertrekTijd']      # 2016-09-27T18:36:00+0200
        vertrektijd = vertrektijd[11:16]          # 18:36
        spoor=  vertrek['VertrekSpoor']
        verbeterdspoort= int(spoor['#text'])
        typetrein=  vertrek['TreinSoort']
        lijst=[vertrektijd,verbeterdspoort,typetrein,eindbestemming]
        #print('Om '+vertrektijd+' vertrekt een' ,typetrein,'op spoor',spoor['#text'], 'naar '+ eindbestemming)
        grotelijst =grotelijst +[lijst]
    return grotelijst

def Sortbijspoor(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l - i - 1):
            if (sub_li[j][1] > sub_li[j + 1][1]):
                tempo = sub_li[j]
                sub_li[j] = sub_li[j + 1]
                sub_li[j + 1] = tempo
    return sub_li


# Driver Code
def gesortopspoor(x):
    newx=Sortbijspoor(x)
    for inf in newx:
        print('Om',inf[0],'vertrekt een',str(inf[2]),'op spoor',inf[1], 'naar ', str(inf[3]))



def Sortbijtijd(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l - i - 1):
            if sub_li[j][0] > sub_li[j + 1][0]:
                tempo = sub_li[j]
                sub_li[j] = sub_li[j + 1]
                sub_li[j + 1] = tempo
    return sub_li
print('\n')
def gesortoptijd(x):
    newx=Sortbijtijd(x)
    for inf in newx:
        print('Om',inf[0],'vertrekt een',str(inf[2]),'op spoor',inf[1], 'naar ', str(inf[3]))


lijst2=getinformation('ut')
#gesortoptijd(grotelijst2)
#gesortopspoor(grotelijst2)
stat=''
while stat=='':
    stat=getstation()

    while stat != '':
        print('wil je dat de informatie op tijd of spoor gesorteerd is ')
        print('als u een ander station wilt selecteren type station in')
        a = input('wat is uw keus')
        if a =='tijd':
            gesortoptijd(lijst2)
            print('\n')
            lijst2 = getinformation(stat)
        if a =='spoor':
            gesortopspoor(lijst2)
            print('\n')
            lijst2 = getinformation(stat)
        if a == 'station':
            stat=''
