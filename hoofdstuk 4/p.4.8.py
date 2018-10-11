def numWords2(filename):
    'returns the number of words in file filename'
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    table = str.maketrans('!,.:;?', 6*' ')
    content=content.translate(table)
    content=content.lower()
    return content.split()
antwoord =numWords2('C:/test.txt')
print(antwoord)