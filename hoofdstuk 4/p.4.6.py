def roster(students):
    'prints average grade for a roster of students'
    print('Last First Class Average Grade')
    for student in students:
            print('{:10}{:10}{:10}{:8.2f}'.format(student[0],student[1], student[2], student[3]))

students = []
students.append(['DeMoines', 'Jim', 'Sophomore', 3.45])
students.append(['Pierre', 'Sophie', 'Sophomore', 4.0])
students.append(['Columbus', 'Maria', 'Senior', 2.5])
students.append(['Phoenix', 'River', 'Junior', 2.45])
students.append(['Olympis', 'Edgar', 'Junior', 3.99])
roster(students)