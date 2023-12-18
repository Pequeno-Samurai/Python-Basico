# Faça um programa que leia uma variável e some 5 caso seja par ou some 8 caso seja ímpar, imprimir o resultado desta operação.

var = int(input("Digite um número: "))

if var % 2 == 0:
    print("Número par, somando 5...")
    var += 5
else:
    print("Número ímpar, somando 8...")
    var += 8

print("Resultado:",var)
