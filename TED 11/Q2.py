# 2. Construa uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos. Depois:
# a. Imprima o resultado da soma de todos os valores da matriz no terminal;
# b. E, criei uma nova matriz B, no qual cada item seja o valor da matriz A * 3;

from random import randint
from copy import deepcopy
import numpy as np

matriz_a, matriz_b, matriz_temp = [],[],[]
soma_total = 0


# matriz_a = [[randint(0,10) for _ in range(10)] for _ in range (10)]
for _ in range(10):
    for i in range (10):
        matriz_temp.append(randint(0,10))
    matriz_a.append(matriz_temp)
    matriz_temp = []

# soma_total = sum(sum(row) for row in matriz_a)

for linha in matriz_a:
    for valor in linha:
        soma_total += valor

matriz_b = deepcopy(matriz_a)

# matriz_b = [[valor for valor in linha] for linha in matriz_a]

for x,i in enumerate(matriz_b):
    for posicao,valor in enumerate(i):
        matriz_b[x][posicao] = valor*3

# matriz_b = [[valor * 3 for valor in row] for row in matriz_a]

print(f'matriz_a {matriz_a}\n')
print(f'Soma total {soma_total}\n')
print(f'matriz_b {matriz_b}')




# matriz_a = np.random.randint(0, 11, (10, 10))

# total_sum = matriz_a.sum()
# print(f'Soma Total matriz_a: {total_sum}')

# matriz_b = matriz_a * 3

# print(f'matriz_a:{matriz_a}\n')
# print(f'matriz_b:{matriz_b}')



