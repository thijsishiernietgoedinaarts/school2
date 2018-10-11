def convert(x):
    y = x * 1.8 + 32
    print(y)

convert(5)

def table(x):
    print('  F', '    C', sep='   ')
    for c in range(-30, 41, 10):
        f = float(c * 1.8 + 32)
        answer= [f,c]
        print('{:^6}{:^9}'.format(f, float(c)))
table(5)