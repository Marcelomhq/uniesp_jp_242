# Desenho de Padrões com Caracteres:
# Contexto: Crie um programa que desenhe padrões simples com caracteres, como triângulos, 
# quadrados ou losangos. Utilize loops aninhados para controlar a quantidade de linhas e colunas e 
# a exibição dos caracteres.

size = int(input("Qual tamanho do quadrado: "))

#Fazendo base e topo do quadrado
print('-'*size)
for i in range(size):
    print("|"+" "*size-2+"|")