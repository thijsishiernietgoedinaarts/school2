infile = open('C:/test.txt', 'r')

content = infile.readlines()
infile.close()

for y in content:
    newcontent = y.split(',')
    print (newcontent[1].strip()+ ', heeft het kaarnummer ' +newcontent[0].strip())
