def seizoen(maand):
    if maand == 3 or maand == 4 or maand == 5:
        print('spring')
    elif maand == 6 or maand == 7 or maand == 8:
        print('summer')
    elif maand == 9 or maand == 10 or maand == 11:
        print('fall')
    elif maand > 12:
        print('error')
    else:
        print('winter')
seizoen(13)