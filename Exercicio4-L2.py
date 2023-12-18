# Crie uma função que receba 3 números inteiros e retorne o maior valor.

def maior_de_tres(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

print("Maior valor: ", maior_de_tres(valor1, valor2, valor3))
