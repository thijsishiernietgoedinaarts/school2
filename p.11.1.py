prijs=4356
def errorexcept():
    try:
        mens=int(input('hoeveel mensen gaan er mee'))
        if mens < 0:
            raise ImportError( "I can't cope with a negative number here.")
        antwoord= prijs/ mens

        print(antwoord)
    except ImportError:
        print('kan geen negatief nummer zijn')
    except ValueError:
        print('vul een getal in niet een woord')
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except:
        print('andere error')


errorexcept()
