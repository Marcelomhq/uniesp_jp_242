# 6. Campeonato de Corrida de Dragões
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
    drag1_km = float(input("Quantos KMs o 1 dragao percorreu? "))
    drag1_time = float(input("E em quanto tempo, em minutos? "))
    drag2_km = float(input("Agora pro Dragao 2, Quantos KMs ele percorreu? "))
    drag2_time = float(input("E em quanto tempo, em minutos? "))

    drag1_speed = drag1_km/drag1_time
    drag2_speed = drag2_km/drag2_time

    if drag1_speed > drag2_speed:
        return f"Dragao 1 eh mais rapido com velocidade de {drag1_speed}KM/mins em relacao a velocidade do Dragao 2 de {drag2_speed}KM/mins."
    elif drag2_speed > drag1_speed:
        return f"Dragao 2 eh mais rapido com velocidade de {drag2_speed}KM/mins em relacao a velocidade do Dragao 1 de {drag1_speed}KM/mins."
    else:
        return f"Os dragoes tem a mesma velocidade de {drag1_speed}KM/mins."
    
if __name__ == "__main__":
    print("Iniciando Arquivo")
    print(winner())
    print("Finalizando Arquivo") 