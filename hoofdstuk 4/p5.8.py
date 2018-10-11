t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]
s = [[0, 1, 2, 0], [0, 1, 1, 1], [0, 1, 0, 0]]
def incr2D(t):
    'increments each number in 2D list of numbers t'
    nrows = len(t) # number of rows
    ncols = len(t[0]) # number of columns

    for i in range(nrows): # i is the row index
        for j in range(ncols): # j is the column index
            t[i][j] += 1

def print2D(t):
    'prints values in 2D list t as a 2D table'
    for row in t:
        for item in row: # print item followed by
            print(item, end=' ') # a blank space
        print() # move to next line

def add2D(t,t2):
    nrows = len(t) # number of rows
    ncols = len(t[0]) # number of columns

    for i in range(nrows):
        for j in range(ncols):
            t[i][j] += t2[i][j]
    print(t)

add2D(s,t)