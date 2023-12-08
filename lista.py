lista = []
index = 0

while True:
    try:
        while True:
            index = index + 1
            valores = int(input(f"Valor {index}: "))
            lista.append(valores)
            if valores <= 0:
                break
        lista.pop()  # remove o ultimo numero digitado por ser negativo.
        print(*lista)
        print("Maior: ", max(lista))
        print("Menor: ", min(lista))
        break
    except ValueError:
        print("Digite somente numeros inteiros")
