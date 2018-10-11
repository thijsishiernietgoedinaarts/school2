def ticker(filepath):
    f = open(filepath, 'r')
    antwoord = {}
    for line in f:
        k, v = line.strip().split(':')
        antwoord[k.strip()] = v.strip()
    f.close()
    return antwoord
cool=ticker('C:/Users/jack/PycharmProjects/untitled/goog.txt')
print(cool)
def prticker(x):
    cool = ticker(x)
    een=input('geef een bedrijfsnaam op')
    twee=input('geef een ticker symbool')
    print('ticker name:',cool[een])
    mbook = {v: k for k, v in cool.items()}
    print('company name:',mbook[twee])

prticker('C:/Users/jack/PycharmProjects/untitled/goog.txt')