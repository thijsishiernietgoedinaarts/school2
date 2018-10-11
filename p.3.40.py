lijst= ['Eleanor', 'Evelyn', 'Sammy', 'Owen', 'Gavin']
def partition(x):
    for y in x:
        if y[0] in 'ABCDEFGHIJKLM':
            print(y)
partition(lijst)