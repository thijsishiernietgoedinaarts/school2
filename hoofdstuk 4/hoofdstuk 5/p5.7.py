def xmult(l1, l2):
    '''returns the list of products of items in list l1
with items in list l2'''
    l = []
    for i in l1:
        for j in l2:
            l.append(i*j)
        print(l)
xmult([2], [1, 5])