# Jogo de Adivinhação:
# Contexto: Implemente um jogo onde o computador escolhe um número aleatório entre 1 e 100,
#  e o usuário tenta adivinhar. Utilize um loop para permitir que o usuário faça várias 
#  tentativas, fornecendo dicas (maior ou menor) a cada tentativa.

from random import randint
random_num = randint(1,100)
try:
    choice = int(input("Digite do numero para tentar adivinhar o numero secreto entre 1 e 100: "))
except ValueError:
    print("voce nao digitou um numero seu alesado.")

while True:
    if choice > random_num:
        print(f"O numero aleatorio eh menor que o seu numero {choice}")
    elif choice < random_num:
        print(f"O numero aleatorio eh maior que o seu {choice}") 
    else:
        print(f"Voce acertou o numero era {random_num}.")
        break
    print("Ok, vou te dar mais uma chance.")
    try:
        choice = int(input("Digite do numero para tentar adivinhar o numero secreto entre 1 e 100: "))
    except ValueError:
        print("voce nao digitou um numero seu alesado.")
    