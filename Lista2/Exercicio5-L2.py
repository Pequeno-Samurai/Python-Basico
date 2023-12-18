# Crie uma função em que receba 3 números inteiros e retorne o menor valor.

def menor_de_tres(x, y, z):
    if x < y and x < z:
        return x
    elif y <= x and y < z:
        return y
    else:
        return z


a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

print("Menor valor: ", menor_de_tres(a, b, c))
