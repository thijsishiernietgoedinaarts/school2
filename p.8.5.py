
def incr2D(t):
    'increments each number in 2D list of numbers t'


    for i in range(10): # i is the row index
        for j in range(10): # j is the column index
            print(i+1,'x',j+1, '=', ((i+1)*(j+1)), end=' ')
        print()


incr2D(5)
