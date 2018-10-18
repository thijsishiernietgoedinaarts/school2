import xmltodict

def proccessXML(filename):
    with open(filename) as myxmlfile:
        filestring = myxmlfile.read()
        xmldictionary = xmltodict.parse(filestring)
        return xmldictionary

productdict= proccessXML('stations.xml')
stationenen= productdict['Stations']['Station']
print('dit is de naam en code van alle stations')
for station in stationenen:
    if station['Namen'] is not None:

        print('{:<6}{:^7}{:>8}'.format(station['Code'],'-', station['Type']))
print('\n' 'dit zijn alle stations met een of meer synoniemen')

for station in stationenen:
    if station['Synoniemen'] is not None:
        print(station['Code'],'-',station['Synoniemen'])

print('\ndit zijn de lange namen van de stations')
for station in stationenen:

        print('{:<6}{:^7}{:<8}'.format(station['Code'], '-', station['Namen']['Lang']))