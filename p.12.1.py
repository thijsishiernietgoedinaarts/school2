import xmltodict

def proccessXML(filename):
    with open(filename) as myxmlfile:
        filestring = myxmlfile.read()
        xmldictionary = xmltodict.parse(filestring)
        return xmldictionary

productdict= proccessXML('marup.xml')
artikels= productdict['artikelen']['artikel']

for artikel in artikels:
    if artikel['naam'] is not None:
        print(artikel['naam'])
