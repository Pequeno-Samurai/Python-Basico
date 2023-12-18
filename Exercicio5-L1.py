#Faça um algoritmo que, dados 3 números inteiros A, B e C, apresente qual dos 3 é o maior e qual é o menor.

while True:
    try:
        a = int(input('Digite o valor de A: '))
        b = int(input('Digite o valor de B: '))
        c = int(input("Digite o valor de C: "))

        if a < b and a < c:
            print("O menor é A")
        elif b <= a and b < c:
            print("O menor é B")
        else:
            print("O menor é C")

        if a > b and a > c:
            print("O maior é A")
        elif b > a and b > c:
            print("O maior é B")
        else:
            print("O maior é C")
        exit()
    except ValueError:
        print("Digite apenas numero inteiros")
