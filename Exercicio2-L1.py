#Faça um programa em Python que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.

while True:
    try:
        a = int(input("Digite o valor de A:"))
        b = int(input("Digite o valor de B:"))
        c = int(input("Digite o valor de C:"))
        if a + b > c:
            print("A soma de A + B e maior que C")
            exit()
        elif a + b == c:
            print("A soma de A + B e igual a C")
            exit()
        else:
            print("A soma de A + B e menor que C")
            exit()
    except ValueError:
        print("Digite apenas numeros inteiros")
