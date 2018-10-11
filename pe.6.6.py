lijst = ['cool beans']
def wijzig(x):
    x.clear()
    x.append('d')
    x.append('e')
    x.append('f')
print(lijst)
wijzig(lijst)
print(lijst)

#je kan de lijst niet veranderen met x=['d','e',f] want dan veranderd hij hem gelijk terug
