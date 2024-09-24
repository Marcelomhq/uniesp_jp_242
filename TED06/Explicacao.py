# Como Escrever em um arquivo de texto
with open('exemplo.txt', 'w') as arquivo:
    arquivo.write("Primeira linha de texto.\n")
    arquivo.write("Segunda linha de texto.\n")

# Como Adicionar informações ao arquivo
with open('exemplo.txt', 'a') as arquivo:
    arquivo.write("Esta é uma linha adicionada posteriormente.\n")

# Como Ler o conteúdo do arquivo
with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:\n", conteudo)