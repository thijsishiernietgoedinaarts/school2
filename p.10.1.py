bruin = {'boxtel','best','beukenlaan','eindhoven','helmond t hout','helmond','helmond brouwhuis deurne'}
groen={'boxtel','best','beukenlaan','eindhoven','geldrop','heeze','weert'}
print('dit zijn de haltes die beide trajecten hebben: ', end='')
for x in bruin:
    if x in groen:
        print(x, end=' ')
antwoord1=bruin-groen
antwoord2=bruin-groen
print('\n''dit zijn de haltes die alleen in bruin voorkomen',str(antwoord1).strip('{''}'))
print('dit zijn de haltes die alleen in groen voorkomen',str(antwoord2).strip('{''}'))