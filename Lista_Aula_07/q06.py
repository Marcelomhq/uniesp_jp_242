# Verificador de Número Primo:
# Contexto: Crie um programa que peça ao usuário um número inteiro e verifique se ele é primo.
# Utilize um loop para testar a divisibilidade do número por outros números menores.

def prime_numb(n):
    if n < 2:
        return False
    for i in range(2,n):
        if i*i > n:
            break
        if n % i == 0:
            return False
    return True

numb = int(input("Digite um numero para checar se ele eh primo? "))
if prime_numb(numb) == False:
    print(f"Numero {numb} nao era primo")
elif prime_numb(numb) == True:
    print(f"Numero {numb} era primo")