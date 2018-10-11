def acro(a):
    list= a.split(' ')
    acronym = ''
    for b in list:
        c= b.capitalize()
        acronym += c[0]

    print(acronym)

acro('Random access memory')
