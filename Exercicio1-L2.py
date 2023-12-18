# Crie uma função que receba um valor e informe se ele é positivo ou não.

def positivo_negativo(valor):
    if valor > 0:
        return True
    else:
        return False


x = int(input("Digite um valor: "))

if positivo_negativo(x):
    print("O valor é positivo")
else:
    print('O valor é negativo')
