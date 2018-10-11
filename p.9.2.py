
while True:
    word=input('gef een wordt van 4 tekens op')
    if len(word) > 4 or len(word) < 4:
        print(word,'heeft', len(word),'letters')
    if len(word) == 4:
        break
print('inlezen van correce string:',word,'is geslaagd')