nieuwwachtwoord = input('nieuwe wachtwoord')
oudwachtwoord = input('oud wachtwoord')
def wachtwoord(x,y):
    if x != y and len(x) > 6:
        for z in x:
            if z in '1234567890':
                return True
    return False


antwoord = wachtwoord(nieuwwachtwoord, oudwachtwoord)
print(antwoord)