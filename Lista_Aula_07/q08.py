# Conversor de Decimal para Binário:
# Contexto: Desenvolva um programa que converta um número decimal fornecido pelo usuário para sua
# representação binária. Utilize um loop para realizar as divisões sucessivas por 2 e armazenar 
# os restos.

def binary(num):
    binary_list = []
    while num > 0:
        binary_list.append(num%2)        
        #num%2 = 1 >>>> lista
        num = num // 2        
        
    return binary_list[5:0:-1]
    # print(reversed(binary_list))
    
    # return ''.join(str(bit) for bit in reversed(binary_list))

numb = int(input("Digite o numero a ser convertido para binario: "))
print(binary(numb))
    
    
