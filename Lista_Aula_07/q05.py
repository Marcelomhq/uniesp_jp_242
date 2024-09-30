# Sequência de Fibonacci:
# Contexto: Desenvolva um programa que gere os primeiros N números da sequência de 
# Fibonacci, onde N é fornecido pelo usuário. Utilize um loop para calcular e exibir os 
# termos da sequência.

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b

num = int(input("Enter the number of fibonacci number that you wanted to be printed.\n"))

i = 1
for current_fib_num in fibonacci(num):    
    print (f"Number {i}: {current_fib_num}")
    i +=1

