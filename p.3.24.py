def enterlist(x):
    for y in x:
        if 'secret' not in y:
            print(y)

enterlist(['cia','secret','mi6','isi','secret'])
