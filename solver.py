from tkinter import *
import random

# Lê apenas palavras com exatamente 5 letras no momento da leitura
with open('palavras_igual_5.txt', "r") as word_list:
    palavras_igual_5 = [word.lower() for word in word_list.read().split('\n') if len(word) == 5]

# Configuração inicial
tela = Tk()
tela.title("Termoo Solver")

pos_letras_verdes = ['', '', '', '', '']
pos_letras_amarelas = ['', '', '', '', '']
lista_letras_cinzas = []

palavra_sugerida = 'areio'

def valida_letras_verdes(palavra):
    return all(
        pos_letras_verdes[i] == '' or pos_letras_verdes[i] == letra
        for i, letra in enumerate(palavra)
    )

def valida_letras_amarelas(palavra):
    for i, letra in enumerate(palavra):
        if pos_letras_amarelas[i] and pos_letras_amarelas[i] == letra:
            return False
    return all(
        letra in palavra for letra in pos_letras_amarelas if letra
    )

def valida_letras_cinzas(palavra):
    return all(
        letra not in palavra or
        (letra in pos_letras_verdes or letra in pos_letras_amarelas)
        for letra in lista_letras_cinzas
    )

def atualiza_listas():
    global palavra_sugerida

    for i, entrada in enumerate(entradas_verdes):
        pos_letras_verdes[i] = entrada.get().lower()

    for i, entrada in enumerate(entradas_amarelas):
        pos_letras_amarelas[i] = entrada.get().lower()

    lista_letras_cinzas.clear()
    for entrada in entradas_cinzas:
        letra = entrada.get().lower()
        if letra:
            lista_letras_cinzas.append(letra)

    palavras_filtradas = [
        palavra for palavra in palavras_igual_5
        if valida_letras_verdes(palavra)
        and valida_letras_amarelas(palavra)
        and valida_letras_cinzas(palavra)
    ]

    palavra_sugerida = random.choice(palavras_filtradas) if palavras_filtradas else 'Nenhuma palavra encontrada'
    label_palavra_sugerida.config(text=f'Palavra Sugerida: {palavra_sugerida}')

# Mensagem de boas-vindas
boas_vindas = Label(tela, text="Encontre o Termoo")
boas_vindas.config(font=("Courier", 14))
boas_vindas.grid(row=0, column=0, columnspan=5, pady=10)

# Letras Verdes ================================================================================================
letras_verdes_label = Label(tela, text="LETRAS VÁLIDAS (VERDES):")
letras_verdes_label.grid(row=1, column=0, columnspan=5, pady=5)

entradas_verdes = []
for i in range(5):
    entrada = Entry(tela, width=2, font=('Arial 24'), justify='center')
    entrada.grid(row=2, column=i, padx=5)
    entradas_verdes.append(entrada)

# Letras Amarelas ==============================================================================================
letras_amarelas_label = Label(tela, text="LETRAS VÁLIDAS (AMARELAS):")
letras_amarelas_label.grid(row=3, column=0, columnspan=5, pady=5)

entradas_amarelas = []
for i in range(5):
    entrada = Entry(tela, width=2, font=('Arial 24'), justify='center')
    entrada.grid(row=4, column=i, padx=5)
    entradas_amarelas.append(entrada)

# Letras Cinzas ================================================================================================
letras_cinzas_label = Label(tela, text="LETRAS INVÁLIDAS (CINZAS):")
letras_cinzas_label.grid(row=5, column=0, columnspan=5, pady=5)

entradas_cinzas = []
for i in range(30):
    row = 6 + (i // 5)  # Começa na linha 6, incrementa para cada grupo de 5
    col = i % 5         # Calcula a coluna (0 a 4)
    entrada = Entry(tela, width=2, font=('Arial 24'), justify='center')
    entrada.grid(row=row, column=col, padx=5)
    entradas_cinzas.append(entrada)

# Botão para atualizar as listas
update_button = Button(tela, text="Atualizar", command=atualiza_listas)
update_button.grid(row=13, column=0, columnspan=5, pady=10)

label_palavra_sugerida = Label(tela, text=f'Palavra Sugerida: {palavra_sugerida}')
label_palavra_sugerida.grid(row=14, column=0, columnspan=5, pady=10)

# Iniciar o loop principal
tela.mainloop()
