# 8. Calculadora de Bônus
# a. Descrição: Um rei deseja distribuir bônus aos seus cavaleiros com 
# base em suas conquistas. Seum cavaleiro completou mais de 10 missões,
# ele recebe um bônus de 100 moedas de ouro. Se
# completou entre 5 e 10 missões, recebe 50 moedas de ouro. 
# Se completou menos de 5, recebe
# 10 moedas de ouro. Crie um programa que receba o número de missões 
# completadas e
# informe o valor do bônus.
# b. Conceito: Desvio condicional aninhado, operadores relacionais.

def rewards(missions):
    if missions > 10:
        return f"Eu como rei, vou recompensar 100 moedas de ouro por suas {missions} missoes completadas!!!"
    elif missions >= 5 and missions <= 10:
        return f"Voce nao foi o melhor cavaleiro, completou apenas {missions} missoes, mas mesmo assim vou te recompensar 50 moedas de ouro."
    else:
        return f"Voce so completou {missions} missoes, isso nao eh digno de um cavaleiro da minha guarda, receba 10 moedas de ouro e melhore!!"

if __name__ == "__main__":
    print("Iniciando Arquivo")
    missions = float(input("Bem-vindo ao meu reino, Quantas missoes voce completou durante sua jornada? "))
    print(rewards(missions))
    print("Finalizando Arquivo") 