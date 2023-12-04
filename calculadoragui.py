import tkinter as tk

def press(key): #Função para receber a entrada do usuario.
    current = entry.get()
    entry.delete(0, tk.END)  
    entry.insert(tk.END, current + str(key))

def clear():
    entry.delete(0, tk.END)  # Limpa a entrada quando o botão 'Limpar' é pressionado

def calculate():
    try:
        result = eval(entry.get())  # Avalia a expressão matemática na entrada
        entry.delete(0, tk.END)  
        entry.insert(tk.END, str(result))  # Insere o resultado na entrada
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erro")  # Se houver um erro durante o cálculo, exibe "Erro" na entrada

root = tk.Tk()  # Inicializa a janela principal
root.title("Calculadora")

root.resizable(False, False)

entry = tk.Entry(root, width=20, font=('Arial', 16), justify='right')  # Cria a entrada para os números e operadores
entry.grid(row=0, column=0, columnspan=4)  # Posiciona a entrada na primeira linha da janela

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', 'X',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=8, height=2, command=lambda key=button: press(key) if key != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1  # Posiciona os botões na interface em uma grade de 4 colunas por 5 linhas

tk.Button(root, text='Limpar', width=8, height=2, command=clear).grid(row=row_val, column=col_val, columnspan=1)  # Adiciona o botão 'Limpar' na última linha

root.mainloop()  # Inicia o loop principal da interface gráfica.
