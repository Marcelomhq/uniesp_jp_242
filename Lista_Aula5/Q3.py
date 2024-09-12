# 3. Adivinhação de Animais
# a. Descrição: Imagine que você é um mago que pode adivinhar o animal favorito das pessoas.
# Crie um programa que pergunte à pessoa se seu animal favorito é mamífero ou réptil. Se for
# mamífero, o programa deve sugerir que é um cachorro; se for réptil, o programa deve sugerir
# que é uma tartaruga.
# b. Conceito: Desvio condicional composto, variáveis.

def advinhe():
    print("Digite o seu tpo de animal favorito: ")
    opcao = int(input('1 - Mamifero ou 2 - Reptil\n'))
    match opcao:
        case 1:
            return "Seu animal favorito eh um cachorro neh"
        case 2:
            return "Seu animal favorito eh uma tartaruga"
if __name__ == "__main__":
    print("Iniciando Arquivo")
    print(advinhe())
    print("Finalizando Arquivo")