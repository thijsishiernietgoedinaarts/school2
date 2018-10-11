def arithemtic(a):
    if len(a) < 2:  # a sequence of length < 2 is arithmetic
        return True
    diff= a[1] - a[0]
    for i in range(1, len(a)-1):
        if a[i+1] - a[i] != diff:
            print( False)
    print(True)
arithemtic([3, 6, 9, 12, 15])