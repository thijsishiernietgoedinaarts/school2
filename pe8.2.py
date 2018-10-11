newlist= []
lijst = eval(input("Geef lijst met minimaal 10 strings: "))
for x in lijst:
        if len(x) == 4:
            newlist.append(x)
print(lijst, '\n' 'De nieuw-gemaakte lijst met alle vier-letter strings is :', newlist)
