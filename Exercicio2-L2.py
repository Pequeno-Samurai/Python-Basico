# Crie uma função que receba 2 números inteiros e retorne o maior valor.

def maior(x, y):
    if x > y:
        return x
    else:
        return y


a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))

print("Maior valor: ", maior(a, b))
