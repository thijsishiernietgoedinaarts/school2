pay= eval(input('hoeveel wordt je betaald'))
uur= eval(input('hoe lang moet je werken'))

if uur>40:
    print('je wordt overuur betaald', uur * pay * 1.5)
else:
    print('je wordt normaal betaald', uur * pay)
