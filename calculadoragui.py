import tkinter as tk #Importa a biblioteca tkinter para a interface gráfica

def press(key): #Função para receber a entrada do usuario.
    current = entry.get() #Obtem o valor atual da entrada
    entry.delete(0, tk.END) #Limpa a entrada
    entry.insert(tk.END, current + str(key)) #Insere o novo valor na entrada

def clear(): #Função para limpar a entrada
    entry.delete(0, tk.END)  # Limpa a entrada quando o botão 'Limpar' é pressionado

def calculate(): #Função para calcular a expressão matemática
    try: #Tenta executar o bloco de código abaixo
        result = eval(entry.get())  # Avalia a expressão matemática na entrada
        entry.delete(0, tk.END) #Limpa a entrada
        entry.insert(tk.END, str(result))  # Insere o resultado na entrada
    except SyntaxError as e: #Se houver um erro durante a execução do bloco try, o bloco except é executado
        entry.delete(0, tk.END) #Limpa a entrada
        entry.insert(tk.END, "Erro de sintaxe")
    except ZeroDivisionError as e: #Se houver um erro durante a execução do bloco try, o bloco except é executado
        entry.delete(0, tk.END) #Limpa a entrada
        entry.insert(tk.END, "Nâo pode dividir por zero")  # Se houver um erro durante o cálculo
    except Exception as e: #Se houver um erro durante a execução do bloco try, o bloco except é executado
        entry.delete(0, tk.END) #Limpa a entrada
        entry.insert(tk.END, "Erro desconhecido")  # Se houver um erro durante o cálculo
 
        
root = tk.Tk()  # Inicializa a janela principal
root.title("Calculadora") #Define o título da janela
root.configure(bg='Black') #Define a cor de fundo da janela

root.resizable(False, False) #Impede que a janela seja redimensionada

entry = tk.Entry(root, width=20, font=('Arial', 16), justify='right', bg='Black',fg='White')  # Cria a entrada para os números e operadores
entry.grid(row=0, column=0, columnspan=4)  # Posiciona a entrada na primeira linha da janela

buttons = [ #Lista com os botões da calculadora
    '7', '8', '9', '/',
    '4', '5', '6', 'X',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1 #Variável para controlar a linha dos botões
col_val = 0 #Variável para controlar a coluna dos botões

for button in buttons: #Loop para criar os botões
    tk.Button(root, text=button, width=8, height=2, command=lambda key=button: press(key) if key != '=' else calculate(), bg='Black', fg='White').grid(row=row_val, column=col_val) #Cria os botões e posiciona na janela
    col_val += 1 #Incrementa a coluna
    if col_val > 3: #Se a coluna for maior que 3
        col_val = 0 #Coluna volta para 0
        row_val += 1  # Posiciona os botões na interface em uma grade de 4 colunas por 5 linhas

tk.Button(root, text='Limpar', width=8, height=2, command=clear, bg='Black',fg='White').grid(row=row_val, column=col_val, columnspan=1)  # Adiciona o botão 'Limpar' na última linha

root.mainloop()  # Inicia o loop principal da interface gráfica.