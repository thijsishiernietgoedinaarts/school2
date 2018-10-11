s = input('Enter square or cube: ')
if s == 'square':
    def f(x):
        'vraagt of het een cube is of een square en dan rekent het het oppervlakte uit'
        return x*x
else:
    def f(x):
        'geeft de averages terug'
        return x*x*x
b= f(3)
help(f)