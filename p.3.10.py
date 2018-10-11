
vowel= 'aeuio'
def noVowel(s):
    for c in s:
        if c in 'aeoiuAEIOU':
            return 'false'
    return 'true'

f = noVowel('cerypt')
print(f)