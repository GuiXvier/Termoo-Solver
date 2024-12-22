from tkinter import *
import random
    
palavras_igual_5 = []

with open('palavras_igual_5.txt', "r") as word_list:
    words = word_list.read().split('\n')
    for word in words:
        palavras_igual_5.append(word.lower())

# Configuração inicial da janela
tela = Tk()
tela.title("Termoo Solver")

lista_letras_verdes = []
lista_letras_amarelas = []
lista_letras_cinzas = []

pos_letras_verdes = ['', '', '', '', '']
pos_letras_amarelas = ['', '', '', '', '']

palavra_sugerida = 'areio'

def filtro_letras_verdes(palavra):
    """
    Filtro para validar palavras com base nas letras verdes.
    """
    
    pontos = 0
    
    # Verifica cada posição da palavra
    for i, letra in enumerate(palavra):
        # Se não há letra verde nessa posição, ignorar
        if pos_letras_verdes[i] == '':
            continue
        # Se a letra coincide com a posição verde, adicionar pontos
        elif letra == pos_letras_verdes[i]:
            pontos += 1
    
    # Adiciona a palavra se ela satisfizer todas as condições
    if pontos == sum(1 for letra in pos_letras_verdes if letra != ''):
        return True
    else:
        return False           

def filtro_letras_amarelas(palavra):
    """
    Verifica se a palavra satisfaz as condições para as letras amarelas.
    """
    for i, letra in enumerate(palavra):
        # Verifica se a letra amarela está na mesma posição que na lista de amarelas
        if pos_letras_amarelas[i] != '' and pos_letras_amarelas[i] == letra:
            return False

    # Verifica se as letras amarelas estão presentes em posições válidas
    for i, letra_amarela in enumerate(pos_letras_amarelas):
        if letra_amarela != '' and letra_amarela not in palavra:
            return False

    return True

def filtro_letras_cinzas(palavra):
    """
    Verifica se a palavra contém letras cinzas em posições inválidas.
    """
    for i, letra in enumerate(palavra):
        # Verifica se a letra está na lista cinza
        if letra in lista_letras_cinzas:
            # Permite se a letra também está nas posições verdes
            if letra in lista_letras_verdes and pos_letras_verdes[i] == letra:
                continue
            # Permite se a letra está como amarela, mas não na posição
            if letra in lista_letras_amarelas and pos_letras_amarelas[i] != letra:
                continue
            # Caso contrário, é inválido
            return False
    return True


def atualiza_listas():
    
    global palavra_sugerida
    global palavras_igual_5
    
    for i, entrada in enumerate(entradas_verdes):
        letra = entrada.get().lower()  # Convertendo para minúsculas
        
        # Se letra != '' armazene essa letra na posição i da lista que contem as letras
        pos_letras_verdes[i] = letra if letra else ''
        if letra:
            lista_letras_verdes.append(letra)
            
    # Atualiza lista de letras amarelas
    for i, entrada in enumerate(entradas_amarelas):
        letra = entrada.get().lower()
        pos_letras_amarelas[i] = letra if letra else ''
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
       if (filtro_letras_verdes(palavra) and filtro_letras_amarelas(palavra) and filtro_letras_cinzas(palavra)):
           palavras_filtradas.append(palavra)
           
    palavras_igual_5 = palavras_filtradas

                    
    print(lista_letras_verdes, lista_letras_amarelas, lista_letras_cinzas)
    print(pos_letras_verdes, pos_letras_amarelas)
    
    palavra_sugerida = palavras_filtradas[random.randint(0, len(palavras_filtradas) - 1)]                
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
