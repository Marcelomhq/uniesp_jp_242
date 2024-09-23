# 9. Escolha de Feitiços
# a. Descrição: Um mago tem três feitiços: fogo, água e terra. 
# Crie um programa que receba a
# escolha do usuário (1 para fogo, 2 para água, 3 para terra) e use o 
# comando match-case para
# exibir o feitiço escolhido.
# b. Conceito: Match-case, variáveis.

def spells(element):
    match element:
        case 1:
            return "FIRE BALL !!!!"
        case 2:
            return "WATER JET !!!"
        case 3:
            return "EARTH TREMOR !!!!"
        case _:
            return "pff ... nothing came out"

if __name__ == "__main__":
    print("Iniciando Arquivo")
    choice = int(input("Mago, qual seu ataque? (1 para fogo, 2 para agua ou 3 para terra) "))
    print(spells(choice))
    print("Finalizando Arquivo") 