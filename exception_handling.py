divisor = float(input("Digite um numero para "))
denominador = float(input("Dividir o numero: "))

try:
    resultado = divisor / denominador
    print("O resultado da divisao é: ", resultado)
except ZeroDivisionError:
    print("Nao é possivel dividir por zero")
except ValueError:
    print("O valor digitado nao é um numero")
except:
    print("Ocorreu um erro desconhecido")
finally:
    print("Obrigado por usar o programa")
    