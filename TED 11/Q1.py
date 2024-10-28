# 1. Faça um algoritmo para ler 10 números e armazenar em um vetor VET, 
# verificar e escrever se existem
# números repetidos no vetor VET e em que posições se encontram.

VET = []
posicoes = []

def receive_numbers():
    for _ in range(10):
        number = int(input("Enter a number: "))
        
        if number in VET:
            for i, x in enumerate(VET):
                if x == number:
                    posicoes.append(i)
            posicoes.append(len(VET))
        VET.append(number)

receive_numbers()

print(VET)
print(posicoes)
            