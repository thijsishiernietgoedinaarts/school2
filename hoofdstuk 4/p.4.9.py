def myGrep(filename, target):
    'prints every line of file filename containing string target'
    infile = open(filename)
    for line in infile:
        if target in line:
            print(line, end='')

myGrep('C:/example.txt','line')