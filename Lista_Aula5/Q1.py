# 1. O Tesouro Escondido
# a. Descrição: Um mapa do tesouro tem duas partes, A e B. A primeira parte está escondida no X
# número de passos para o norte, e a segunda no Y número de passos para o leste. Crie um
# programa que receba os valores de X e Y e calcule a distância total que o pirata precisa
# percorrer para chegar ao tesouro (soma de X e Y).
# b. Conceito: Operadores aritméticos, variáveis.
def coordernadas():
    x = 10
    y = 27

    total_percorrido = x+y
    return f"Distancia total percorrida: {total_percorrido}kms."


if __name__ == "__main__":
    print("Iniciando Arquivo")
    print(coordernadas())
    print("Finalizando Arquivo")