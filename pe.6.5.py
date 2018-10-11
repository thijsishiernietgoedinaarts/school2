grondgetallen=[1, 5 ,6 ,-20]
def kwadraten_som(lijst):
    som = 0
    for item in lijst:
        if item > 0:
            som= som + item**2

    return som


print(kwadraten_som(grondgetallen))
