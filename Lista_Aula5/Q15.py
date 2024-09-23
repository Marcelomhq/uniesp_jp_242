# 15. Portal de Viagem no Tempo
# a. Descrição: Um cientista está criando um portal de viagem no tempo que só pode ser ativado se
# todos os parâmetros estiverem corretos: energia acima de 80%, coordenadas de destino
# precisas, e o tempo ajustado corretamente. Crie um programa que receba esses valores e use
# operadores lógicos para verificar se o portal pode ser ativado. Se qualquer parâmetro estiver
# incorreto, o programa deve indicar qual é o problema.
# b. Conceito: Operadores lógicos, relacionais, desvio condicional aninhado.

def time_travel_check(): 

    try:
        energy = float(input("Quanto de energia temos restante na maquina? "))
    except ValueError:
        return "Erro: O valor de energia deve ser um número. Tente novamente."

    try:
        coord_x = float(input("Qual a coordenada x destino? "))
    except ValueError:
        return "Erro: A coordenada x deve ser um número. Tente novamente."

    try:
        coord_y = float(input("Qual a coordenada y destino? "))
    except ValueError:
        return "Erro: A coordenada y deve ser um número. Tente novamente."

    try:
        time = int(input("Qual o ano que voce quer ir? "))
    except ValueError:
        return "Erro: O ano deve ser um número inteiro. Tente novamente."

    if energy > 80:
        return f"Viagem AUTORIZADA, até o ano de {time}!"
    
    return "Algo deu errado, boa sorte na próxima vez."

if __name__ == "__main__":
    print(time_travel_check())
    


