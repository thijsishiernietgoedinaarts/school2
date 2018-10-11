
def alleven(x):
    for c in x: #hier wordt c aangegeven
        if c % 2 ==1: #hier wordt c gebruikt
            return 'false'
    return 'true'

f = alleven([12, 8, 0, -1, 4, -6, 10])
print(f)