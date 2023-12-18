#Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprimindo o resultado.

while True:
    try:
        numero = int(input("Digite um número: "))

        if numero > 0:
            print("O número é positivo\nDobro = ", numero * 2)
            exit()
        else:
            print("O número é negativo\nTriplo = ", numero * 3)
            exit()
    except ValueError:
        print("O valor digitado não é um número inteiro")
