studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]
import math
def gemiddelde_per_student(studentencijfers):
    'increments each number in 2D list of numbers t'
    nrows = len(studentencijfers)  # number ofgemiddelde_per_student rows
    ncols = len(studentencijfers[0])  # number of columns
    antwoord= []
    for i in studentencijfers:  # i is the row index
        antwoord.append ((i[0]+i[1]+i[2])/3)
    return(antwoord)
def gemiddelde_van_alle_studenten(studentencijfers):
    antwoord2=sum(gemiddelde_per_student(studentencijfers))/4
    return antwoord2
#antwoord += ((i[0]+i[1]+i[2])/3)
    #print(antwoord)
print (gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))
print(round(gemiddelde_van_alle_studenten(studentencijfers)))
