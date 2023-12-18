#Faça um programa que leia dois valores inteiros A e B se os valores forem iguais deverá se somar os dois,
#caso contrário multiplique A por B. Ao final de qualquer um dos cálculos deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na tela.

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))

if a == b:
    print("A e B são iguais, somando...")
    c = a + b
else:
    print("A e B são diferentes, multiplicando...")
    c = a * b

print("O valor de C é:", c)
