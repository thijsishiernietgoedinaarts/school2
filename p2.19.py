answers = ['Y', 'N', 'N', 'Y', 'N', 'Y', 'Y', 'Y', 'N', 'N', 'N']
numyes =answers.count('Y')
numno = answers.count('N')
percentyes= numyes / (numno+numyes) * 100
answers.sort()

f= answers.index('Y')
