x2 = int(input())
y2 = int(input())


def distEuclid(x2, y2):
    dd = ((x2 - 15)**2 + (y2 - (-2))**2)**(1/2)
    return dd



valorf = distEuclid(x2, y2)
print("distancia Euclidiana = {:.2f}".format(valorf))