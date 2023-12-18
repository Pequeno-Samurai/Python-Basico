lista = [1, 3, 5, 7, 9] #usa [] e seus elementos podem ser modificados
lista.append(11) #adiciona um elemento no final da lista
print("Elementos da minha lista:",*lista)

tupla = (2, 2, 2, 4, 6, 8, 10) #usa () e seus elementos não podem ser modificados
print("Elementos da minha tupla:",*tupla)
print("O numero 2 aparece",tupla.count(2), "vezes na tupla") #conta quantas vezes o elemento aparece na tupla

conjunto = {1, 2, 3, 3, 4, 5} #usa {} e seus elementos não podem ser repetidos
print("Elementos do meu conjunto:",*conjunto)

dicionario = {'nome': 'João', 'idade': 25} #usa {} e seus elementos são compostos por chave:valor
print("Elementos do meu dicionario:",*dicionario)