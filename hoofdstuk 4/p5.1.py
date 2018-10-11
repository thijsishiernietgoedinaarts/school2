def myBMI(weight, height):
    'prints BMI report'
    bmi = weight * 703 / height**2
    if bmi < 18.5:
        print('Underweight')
    elif bmi < 25:
        print('Normal')
    else: # bmi >= 25
        print('Overweight')