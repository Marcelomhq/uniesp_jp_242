def army():
    army = int(input("Aonde esta o exercito do rei? \n1 - Dentro\nou\n2 - Fora\n"))
    if army == 1: return True
    elif army == 2: return False
    

def activate_defense(army_inside):
    match army_inside:
        case False:
            return "ATIVAR defesas magicas!!!!"
        case True:
            return "O exercito esta aqui, nao eh necessario ativar as defesas magicas."
if __name__ == "__main__":
    print(activate_defense(army()))