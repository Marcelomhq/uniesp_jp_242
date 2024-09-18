# 10. A Caverna dos Desafios
# a. Descrição: Um aventureiro encontrou uma caverna cheia de portas,
# cada uma com um número de 1 a 5. Atrás de cada porta há um desafio. 
# Crie um programa que receba o número da porta escolhido pelo aventureiro 
# e use match-case para mostrar qual desafio ele enfrentará.
# b. Conceito: Match-case, operadores relacionais.

def challenge(choice):
    while True:
        match choice:
            case 1: 
                print("You'll have to face this 10ft tall OGRE. MUAHAHA") 
                break
            case 2: 
                print("You'll have to face a copy of yourself in a deadly challenge!!")
                break
            case 3: 
                print("In front of you there's a deadly obstacle course, in order to get out you will have to go through it.")
                break
            case 4: 
                print("In order to go through you will have to pay a fee of 1000 gold pieces.")
                break
            case 5:
                print("LUCKY CHOICE, you can go through without any problems.")
                break
            case _: 
                choice = int(input("Invalid option, remember you can't walk back, you MUST choose a door. What's your choice of door again? "))


if __name__ == "__main__":
    choice = int(input("Welcome to the final challenge, you can't walk back and you will have to choose between 5 doors.\n What's you choice? "))       
    challenge(choice)  