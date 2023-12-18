#O IMC – Índice de Massa Corporal é um critério da Organização Mundial de Saúde para dar uma indicação sobre a condição 
#de peso de uma pessoa adulta. A fórmula é IMC = peso / ( altura * altura). Elabore um programa que leia o peso e a 
#altura de um adulto e mostre sua condição de acordo com a tabela abaixo: IMC em adultos Condição: 
#a) Abaixo de 18,5 “Abaixo do peso” b) Entre 18,5 e 25 “Peso normal” c) Entre 25 e 30 “Acima do peso” d) Acima de 30 “obeso

while True:
    try:
        peso = float(input("Digite seu peso: "))
        altura = float(input("Digite sua altura: "))

        imc = peso / (altura * altura)

        if imc < 18.5:
            print("Abaixo do peso")
        elif imc >= 18.5 and imc < 25:
            print("Peso normal")
        elif imc >= 25 and imc < 30:
            print("Sobrepeso")
        elif imc >= 30 and imc < 35:
            print("Obeso leve")
        elif imc >= 35 and imc < 40:
            print("Obeso moderado")
        else:
            print("Obeso mórbido")
        exit()
    except ValueError:
        print("Erro: Digite apenas números")

