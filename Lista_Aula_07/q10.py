# Simulador de Lançamento de Dados:
# Contexto: Implemente um programa que simule o lançamento de um dado de 
# 6 faces várias vezes, conforme especificado pelo usuário. 
# Utilize um loop para realizar os lançamentos e exibir os resultados.

from random import randint

def dice(attempts):
    results_list = [] #None
    for _ in range(attempts):
        # print(randint(1,6))
        results_list.append(randint(1,6))
    return results_list

attempts = int(input('Quantas vezes voce quer girar o dado? '))
print(dice(attempts))

# results = dice(attempts) #results = results_list
# for index, n in enumerate(results):
#     print(f"Dice attempt:{index+1} had the result of {n}.")
    


