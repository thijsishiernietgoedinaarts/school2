import datetime


newfile= open("C:/Users/jack/Documents/hardloop.txt", "w+")
for i in range(5):
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d %b %Y, %H:%M:%S")
    newfile.write(input("geef naam")+' '+s +'\n')
content = newfile.readlines()
print(content)


newfile.close()
