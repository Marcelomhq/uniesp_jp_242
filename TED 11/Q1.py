# 1. Faça um algoritmo para ler 10 números e armazenar em um vetor VET, 
# verificar e escrever se existem
# números repetidos no vetor VET e em que posições se encontram.

VET = []
posicoes = set()

def receive_numbers():
    for o in range(10):
        number = int(input("Enter a number: "))
        
        if number in VET:
            for i, x in enumerate(VET):
                if x == number:
                    posicoes.add(i)
            posicoes.add(len(VET))
        VET.append(number)

receive_numbers()

print(VET)
print(posicoes)

# VET = []
# posicoes = {}

# def receive_numbers():
#     for j in range(10):
#         number = int(input("Enter a number: "))
        
#         if number in VET:
#             if number in posicoes:
#                 positions[number].append(j)
#             else:
#                 positions[number] = [VET.index(number), j]
#         VET.append(number)

# receive_numbers()

# print("VET:", VET)
# print("posicoes repetidas:", posicoes)
