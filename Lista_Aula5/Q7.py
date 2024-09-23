# 7. Classificação de Plantas Mágicas
# a. Descrição: Um botânico está classificando plantas mágicas em uma 
# floresta. Ele quer saber se
# uma planta é pequena (menos de 1 metro), média (entre 1 e 3 metros),
# ou grande (mais de 3
# metros). Crie um programa que receba a altura da planta e informe a
# sua classificação.
# b. Conceito: Operadores relacionais, desvio condicional aninhado.

def plant(height):
    if height < 1:
        return "Planta magica eh pequena"
    elif height >= 1 and height <= 3:
        return "Planta magica tem altura mediana"
    else:
        return "CARAMBA!!! Planta magica grande"


if __name__ == "__main__":
    print("Iniciando Arquivo")
    height = float(input("Qual a altura da planta magica? "))
    print(plant(height))
    print("Finalizando Arquivo") 