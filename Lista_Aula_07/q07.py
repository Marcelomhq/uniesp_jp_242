# Calculadora de Fatorial:
# Contexto: Implemente um programa que calcule o fatorial de um número fornecido pelo usuário.
# Utilize um loop para realizar as multiplicações necessárias.

def factorial(num):
    result = 1
    if num == 0 or num ==1:
        return 1
    for i in range(2,num+1):
        result *= i
    return result

numb = int(input("Digite o numero para mostramos seu fatorial: "))
print(factorial(numb))