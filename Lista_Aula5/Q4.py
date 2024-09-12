# 4. Contagem de Moedas
# a. Descrição: Um colecionador de moedas tem 3 tipos de moedas: de 1 real, de 50 centavos e de
# 25 centavos. Escreva um programa que receba a quantidade de cada tipo de moeda e calcule o
# valor total que o colecionador tem.
# b. Conceito: Operadores aritméticos, tipos de dados (float).

def moedas():
    moeda1 = int(input("Para saber quanto dinheiro voce tem, primeiro temos que saber quantas moedas voce tem, entao nos diga:\nQuantas moedas de 1 Real voce possui? "))
    moeda50 = int(input("Agora quantas moedas de 0,50 centavos voce possui: "))
    moeda25 = int(input("E por ultimo quantas moedas de 25 centavos? "))

    total = moeda1 + (moeda50 * 0.5) + (moeda25 * 0.25)

    return total


if __name__ == "__main__":
    print("Iniciando Arquivo")
    print(f"Seu valor total eh de: {moedas()}R$.")
    print("Finalizando Arquivo")