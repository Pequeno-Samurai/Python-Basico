# Crie uma função que receba 2 números inteiros e retorne o menor valor.

def menor(x, y):
    if x < y:
        return x
    else:
        return y


valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))

print("Menor valor: ", menor(valor1, valor2))
