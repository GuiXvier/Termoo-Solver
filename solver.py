from tkinter import *
import random

# Lê apenas palavras com exatamente 5 letras no momento da leitura
# A lista de palavras é carregada a partir de um arquivo texto chamado 'palavras_igual_5.txt'
with open('palavras_igual_5.txt', "r") as word_list:
    palavras_igual_5 = [word.lower() for word in word_list.read().split('\n') if len(word) == 5]

# Configuração inicial da interface
tela = Tk()
tela.title("Termoo Solver")  # Define o título da janela

# Variáveis globais para armazenar as restrições do jogo
pos_letras_verdes = ['', '', '', '', '']  # Lista para letras confirmadas nas posições corretas
pos_letras_amarelas = ['', '', '', '', '']  # Lista para letras corretas, mas em posições erradas
lista_letras_cinzas = []  # Lista para letras descartadas (não pertencem à palavra)

# Inicializa a sugestão de palavra com uma escolha padrão
palavra_sugerida = 'areio'

# Função para validar se uma palavra atende às restrições de letras verdes
def valida_letras_verdes(palavra):
    return all(
        pos_letras_verdes[i] == '' or pos_letras_verdes[i] == letra
        for i, letra in enumerate(palavra)
    )

# Função para validar se uma palavra atende às restrições de letras amarelas
def valida_letras_amarelas(palavra):
    for i, letra in enumerate(palavra):
        # Verifica se há letras amarelas na mesma posição (não permitido)
        if pos_letras_amarelas[i] and pos_letras_amarelas[i] == letra:
            return False
    # Verifica se todas as letras amarelas estão presentes na palavra
    return all(
        letra in palavra for letra in pos_letras_amarelas if letra
    )

# Função para validar se uma palavra atende às restrições de letras cinzas
def valida_letras_cinzas(palavra):
    return all(
        letra not in palavra or
        (letra in pos_letras_verdes or letra in pos_letras_amarelas)
        for letra in lista_letras_cinzas
    )

# Função para atualizar as listas de letras e filtrar as palavras possíveis
def atualiza_listas():
    global palavra_sugerida

    # Atualiza a lista de letras verdes com base na entrada do usuário
    for i, entrada in enumerate(entradas_verdes):
        pos_letras_verdes[i] = entrada.get().lower()

    # Atualiza a lista de letras amarelas com base na entrada do usuário
    for i, entrada in enumerate(entradas_amarelas):
        pos_letras_amarelas[i] = entrada.get().lower()

    # Atualiza a lista de letras cinzas com base na entrada do usuário
    lista_letras_cinzas.clear()
    for entrada in entradas_cinzas:
        letra = entrada.get().lower()
        if letra:
            lista_letras_cinzas.append(letra)

    # Filtra as palavras com base nas validações (letras verdes, amarelas e cinzas)
    palavras_filtradas = [
        palavra for palavra in palavras_igual_5
        if valida_letras_verdes(palavra)
        and valida_letras_amarelas(palavra)
        and valida_letras_cinzas(palavra)
    ]

    # Escolhe uma palavra aleatória entre as filtradas ou exibe uma mensagem de erro
    palavra_sugerida = random.choice(palavras_filtradas) if palavras_filtradas else 'Nenhuma palavra encontrada'
    label_palavra_sugerida.config(text=f'Palavra Sugerida: {palavra_sugerida}')

# Mensagem de boas-vindas no topo da janela
boas_vindas = Label(tela, text="Encontre o Termoo")
boas_vindas.config(font=("Courier", 14))
boas_vindas.grid(row=0, column=0, columnspan=5, pady=10)

# Seção para entrada de letras verdes (confirmadas)
letras_verdes_label = Label(tela, text="LETRAS VÁLIDAS (VERDES):")
letras_verdes_label.grid(row=1, column=0, columnspan=5, pady=5)

entradas_verdes = []
for i in range(5):
    entrada = Entry(tela, width=2, font=('Arial 24'), justify='center')  # Cria entradas para cada posição
    entrada.grid(row=2, column=i, padx=5)
    entradas_verdes.append(entrada)

# Seção para entrada de letras amarelas (corretas em posições erradas)
letras_amarelas_label = Label(tela, text="LETRAS VÁLIDAS (AMARELAS):")
letras_amarelas_label.grid(row=3, column=0, columnspan=5, pady=5)

entradas_amarelas = []
for i in range(5):
    entrada = Entry(tela, width=2, font=('Arial 24'), justify='center')
    entrada.grid(row=4, column=i, padx=5)
    entradas_amarelas.append(entrada)

# Seção para entrada de letras cinzas (descartadas)
letras_cinzas_label = Label(tela, text="LETRAS INVÁLIDAS (CINZAS):")
letras_cinzas_label.grid(row=5, column=0, columnspan=5, pady=5)

entradas_cinzas = []
for i in range(30):  # Permite até 30 entradas de letras cinzas
    row = 6 + (i // 5)  # Calcula a linha com base na posição
    col = i % 5         # Calcula a coluna com base na posição
    entrada = Entry(tela, width=2, font=('Arial 24'), justify='center')
    entrada.grid(row=row, column=col, padx=5)
    entradas_cinzas.append(entrada)

# Botão para atualizar as listas e sugerir uma palavra
update_button = Button(tela, text="Atualizar", command=atualiza_listas)
update_button.grid(row=13, column=0, columnspan=5, pady=10)

# Rótulo para exibir a palavra sugerida
label_palavra_sugerida = Label(tela, text=f'Palavra Sugerida: {palavra_sugerida}')
label_palavra_sugerida.grid(row=14, column=0, columnspan=5, pady=10)

# Inicia o loop principal da interface gráfica
tela.mainloop()
