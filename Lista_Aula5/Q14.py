# 14. O Julgamento do Sábio
# a. Descrição: Um sábio está julgando um duelo entre dois guerreiros. Ele quer saber qual
# guerreiro deve ser considerado vencedor, com base em suas habilidades de ataque e defesa.
# Crie um programa que receba os valores de ataque e defesa dos dois guerreiros e determine o
# vencedor (aquele com maior soma de ataque e defesa). Se houver empate, o programa deve
# considerar a defesa como critério de desempate.
# b. Conceito: Operadores aritméticos, relacionais, desvio condicional aninhado.

def winner():
    atk1 = int(input("Guerreiro 1: Qual seu ataque? "))
    def1 = int(input("E agora, sua defesa? "))
    atk2 = int(input("Guerreiro 2, sua vez !!! Qual seu ataque? "))
    def2 = int(input("E sua defesa? "))
    warrior1 = atk1+def1
    warrior2 = atk2+def2
    if warrior1 == warrior2:
        if def1 == def2:
            return f"Impressionante!!! EMPATE!! Os guerreiros tem a mesma media de atk e def de: {warrior1} e suas defesas sao iguais de: {def1}"
        if def1 > def2:
            return f"Guerreiro 1 eh vencedor por criterio de desempate por causa da sua defesa de {def1}"
        else:
            return f"Guerreiro 2 eh o vencedor por criterio de desempate por causa da sua defesa de {def2}"
    elif warrior1 > warrior2:
        return f"Guerreiro 1 eh vencedor com sua media de atk e def de {warrior1}"
    else:
        return f"Guerreiro 2 eh vencedor com sua media de atk e def de {warrior2}"
    
if __name__ == "__main__":
    print(winner())