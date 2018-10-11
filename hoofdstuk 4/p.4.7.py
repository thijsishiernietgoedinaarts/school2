def hoeveel(filename,line):
    'returns the number of characters in file filename'
    infile = open(filename, 'r')
    content = infile.read()
    answer= content.count(line)
    infile.close()

    print(answer)
hoeveel('C:/test - kopie.txt', 'line')