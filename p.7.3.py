infile = open('C:/test.txt', 'r')

content = infile.readlines()
infile.close()
highest = max(content)

for y in content:
    newcontent = y.split(',')
    lijst=(newcontent[1].strip()+ ', heeft het kaarnummer ' +newcontent[0].strip())

print(lijst.find('645345'))
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

lengte=file_len('C:/test.txt')

print('deze file telt', lengte, '\n' 'het grootste kaartnummer is:', highest, 'en staat op regel', )