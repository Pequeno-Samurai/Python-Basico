import random

lista = []

i = 0
while True:
    i = i + 1
    number = random.randint(0, 10000)
    lista.append(number)
    if i == 99999:
        break

print("Valores aleatórios: ", lista)
print("Maior valor: ", max(lista))
print("Menor valor: ", min(lista))
print("Quantas vezes o maior valor apareceu: ", lista.count(max(lista)))
print("Quantas vezaes o menor valor apareceu: ", lista.count(max(lista)))

