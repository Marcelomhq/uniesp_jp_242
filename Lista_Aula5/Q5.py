# 5. Jornada no Deserto

# a. Descrição: Um explorador está cruzando um deserto. Ele precisa saber se a quantidade de
# água que tem é suficiente para chegar ao próximo oásis. Ele calcula que precisa de 2 litros de
# água para cada quilômetro. Crie um programa que receba a quantidade de água disponível e a
# distância até o oásis, e informe se a água é suficiente.
# b. Conceito: Operadores aritméticos, desvio condicional simples.

def water_needed():
    water = float(input("Quantos Litros de agua voce possui? "))
    dist = float(input("Quantos KMs faltam pra chegar ate o Oasis? "))

    if dist <= water/2:
        return "Voce possui agua suficiente pra chegar tranquilo no oasis, va com deus."
    else:
        return "Voce nao tem agua suficiente pra chegar no oasis, va buscar mais agua. "

if __name__ == "__main__":
    print("Iniciando Arquivo")
    print(water_needed())
    print("Finalizando Arquivo")