import random
def monopolyworp():
    worp1= random.randint(1,7)
    worp2= random.randint(1,7)
    print(worp1,'+',worp2,'=',worp1+worp2, end=' ')
    if worp1 == worp2:
        print('(dubbel)')
        worp3 = random.randint(1, 7)
        worp4 = random.randint(1, 7)
        print(worp3, '+', worp4, '=', worp3 + worp4, end=' ')
        if worp3 == worp4:
            print('(dubbel)')
            worp5 = random.randint(1, 7)
            worp6 = random.randint(1, 7)
            print(worp5, '+', worp6,'=', end=' ')
            if worp5 == worp6:
                print( 'ga naar de gevangenis')
            else:
                print(worp5+worp6)
monopolyworp()