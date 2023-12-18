#Faça um algoritmo que simule um caixa eletrônico. O usuário informa o valor que deseja sacar, o caixa eletrônico verifica se o valor é menor que o saldo disponível e se, o valor é inferior ao saldo, 
#informa que o saque será liberado, enquanto que, se o valor for maior que o saldo, informar ao usuário que o saque excedeu o saldo na conta. Assuma um saldo de $10.000,00 de saldo disponível para o saque.

saldo = 1000

while True:
    try:
        saque = float(input("Digite o valor do saque: "))
        if saque > saldo:
            print("Saldo insuficiente")
        else:
            saldo = saldo - saque
            print("Saque realizado com sucesso")
            print("Saldo atual: ", saldo)
            exit()
    except ValueError:
        print("Digite um valor em numeros por favor !")
