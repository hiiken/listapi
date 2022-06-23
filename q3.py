d = float(input())
b = float(input())

def versetzt(d, b):
    f = 2/((2/(3*d) + 2/(4*b)))
    return f

valorf = versetzt(d, b)

print("f = {:.2f}".format(valorf))