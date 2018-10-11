def powers(n):
    'prints 2**i for i = 1, 2, ..., n'
    for i in range(1, n+1):
        print(2**i, end=' ')
powers(7)