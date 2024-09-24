# 6. Campeonato de Corrida de Dragões
# a. Descrição: Em um campeonato de corrida de dragões, 
# cada dragão corre uma determinada
# distância em um certo tempo. Crie um programa que receba a 
# distância e o tempo de dois
# dragões diferentes e determine qual dragão é mais rápido, 
# ou se ambos têm a mesma
# a. Descrição: Em um campeonato de corrida de dragões, 
# cada dragão corre uma determinada
# distância em um certo tempo. Crie um programa que receba a 
# distância e o tempo de dois
# dragões diferentes e determine qual dragão é mais rápido, 
# ou se ambos têm a mesma
# velocidade.
# b. Conceito: Operadores aritméticos, operadores relacionais, 
# desvio condicional composto.

def winner():
    dist = 1000
    drag1_time = float(input("Em quantas horas o dragao 1 percorreu nosso percurso? "))    
    drag2_time = float(input("Em quantas horas o dragao 2 percorreu nosso percurso? "))

    drag1_speed = dist/drag1_time
    drag2_speed = dist/drag2_time

    if drag1_speed > drag2_speed:
        print(f"Dragao 1 eh mais rapido com velocidade de {drag1_speed}KM/h em relacao a velocidade do Dragao 2 de {drag2_speed}KM/h.")
    elif drag2_speed > drag1_speed:
        print(f"Dragao 2 eh mais rapido com velocidade de {drag2_speed}KM/h em relacao a velocidade do Dragao 1 de {drag1_speed}KM/h.")
    else:
        print(f"Os dragoes tem a mesma velocidade de {drag1_speed}KM/h.")
    
if __name__ == "__main__":
    print("Iniciando Arquivo")
    vencedor = winner()
    print(f"Imprimindo vencedor {vencedor}")

    # salvar ele num arquivo de texto 
    print("Finalizando Arquivo") 
    