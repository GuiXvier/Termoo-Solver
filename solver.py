import tkinter as tk
from tkinter import *
import random

palavras_igual_5 = []

with open('palavras_igual_5.txt', "r") as word_list:
    words = word_list.read().split('\n')
    for word in words:
        palavras_igual_5.append(word)

# Configuração inicial da janela
tela = Tk()
tela.title("Termoo Solver")

lista_letras_verdes = []
lista_letras_amarelas = []
lista_letras_cinzas = []

pos_letras_verdes = ['', '', '', '', '']

palavra_sugerida = 'areio'

def atualiza_listas():
    
    global palavra_sugerida
    # Função clear() apaga todos os elementos da lista
    lista_letras_verdes.clear()
    """
        Se lê "Para cada índice i e valor entrada dentro da lista entradas_verdes"
        
        enumerate(entradas_verdes) => A função enumerate() retorna uma sequência de pares (índice, valor) 
        para cada elemento da lista entradas_verdes.
    """
    for i, entrada in enumerate(entradas_verdes):
        letra = entrada.get().lower()  # Convertendo para minúsculas
        
        # Se letra != '' armazene essa letra na posição i da lista que contem as letras
        pos_letras_verdes[i] = letra if letra else ''
        if letra:
            lista_letras_verdes.append(letra)

    # Atualiza lista de letras amarelas
    for entrada in entradas_amarelas:
        letra = entrada.get().lower()
        if letra:
            lista_letras_amarelas.append(letra)

    # Atualiza lista de letras cinzas
    for entrada in entradas_cinzas:
        letra = entrada.get().lower()
        if letra:
            lista_letras_cinzas.append(letra)

   # Filtra palavras baseadas nas condições
    palavras_filtradas = []
    for palavra in palavras_igual_5:
        # Ignorar palavras que não têm exatamente 5 caracteres
        if len(palavra) != 5:
            continue

        # Filtro de letras verdes (posição exata ou contagem suficiente)
        """
            Para cada índice i de 0 a 4 (ou seja, nas 5 posições), verifica se a letra na posição i da palavra (palavra[i]) 
            é igual à letra verde correspondente na mesma posição (pos_letras_verdes[i]) ou se não há uma letra definida 
            para aquela posição (ou seja, pos_letras_verdes[i] é uma string vazia).
        """
        letras_verdes_validas = all(
            palavra[i] == pos_letras_verdes[i] or pos_letras_verdes[i] == '' 
            for i in range(5)
        )
        
        # Se a palavra não passar no filtro de letras verdes, então pule para a próxima palavra
        if not letras_verdes_validas:
            continue

        # Filtro de letras amarelas (presente, mas em qualquer posição, exceto na posição verde)
        letras_amarelas_validas = True
        for letra in lista_letras_amarelas:
            if letra in palavra:
                # Certificar-se de que a letra amarela não está na posição onde é verde
                for i in range(5):
                    if pos_letras_verdes[i] == letra and palavra[i] == letra:
                        letras_amarelas_validas = False
                        break
                # Nova verificação: garantir que a letra amarela não ocupe a mesma posição de uma outra letra amarela
                for i in range(5):
                    if palavra[i] == letra and letra == lista_letras_amarelas[0]:  # Comparando com a letra amarela que já foi processada
                        if i == lista_letras_amarelas.index(letra):  # Se estiver na mesma posição de outra letra amarela, invalidar
                            letras_amarelas_validas = False
                            break

            if not letras_amarelas_validas:
                break

        if letras_amarelas_validas:
            # Filtro de letras cinzas (não pode conter)
            if all(letra not in palavra for letra in lista_letras_cinzas):
                palavras_filtradas.append(palavra)

        # Filtro de letras cinzas (não pode conter excessos além do esperado)
        """
            Garante que a quantidade de vezes que a letra aparece na palavra não seja maior do que o número total de vezes que essa letra pode 
            aparecer, levando em consideração tanto as letras amarelas (que podem aparecer em qualquer posição) 
            quanto as letras verdes (que devem aparecer em uma posição específica).
        """
        letras_cinzas_validas = all(
            palavra.count(letra) <= lista_letras_amarelas.count(letra) + pos_letras_verdes.count(letra)
            for letra in lista_letras_cinzas
        )

        if letras_cinzas_validas:
            palavras_filtradas.append(palavra)

                    
    print(lista_letras_verdes, lista_letras_amarelas, lista_letras_cinzas)
    print(pos_letras_verdes)
    
    palavra_sugerida = palavras_filtradas[0]                
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
