z = float(input())
b = float(input())
h = float(input())


def equac(z, b, h):
    cox = ((z**3) + (b**2) + h)/(z*b*h)
    return cox

valorcox = equac(z, b, h)
print("cox = {:.2f}".format(valorcox))