x = - 11
y = int(input())
z = int(input())


def calcula_maior(n1, n2):
    maior = (n1 + n2 + abs(n1 - n2))/2
    return maior

maior1 = calcula_maior(y, z)
maior2 = calcula_maior(maior1, x)

print("O maior inteiro: {:.0f}".format(maior2))