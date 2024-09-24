# # 12. A Batalha Final
# # a. Descrição: Um herói precisa decidir qual arma usar na batalha final. Ele tem três armas: uma
# # espada, um arco e uma lança. Cada arma tem um poder de ataque e uma durabilidade. A
# # escolha deve considerar que o poder de ataque seja maior que 50 e a durabilidade maior que
# # 70. Crie um programa que receba os valores de ataque e durabilidade das três armas e
# # determine qual é a mais adequada. Se nenhuma atender, o programa deve sugerir que o herói
# # busque uma nova arma.
# # b. Conceito: Operadores lógicos, relacionais, desvio condicional aninhado.

def final_battle():

    espada_atk = int(input("digite atk: "))
    espada_durability = int(input(("durabilidade")))
    bow_atk = int(input("digite atk: "))
    bow_durability = int(input(("durabilidade")))
    spear_atk = int(input("digite atk: "))
    spear_durability = int(input(("durabilidade")))
    espada_boa,bow_boa,spear_boa = False,False,False
    if espada_atk > 50 and espada_durability >70:
        espada_boa = True

    if bow_atk> 50 and bow_durability >70:
        bow_boa = True

    if spear_atk >50 and spear_durability >70:
        spear_boa = True

    if espada_boa and bow_boa and spear_boa:
        return "AS tres arma sao validas, va com as 3"
    elif espada_boa and bow_boa:
        return "espada e bow boas"
    elif espada_boa and spear_boa:
        return "espada and spear boas"
    elif spear_boa and bow_boa:
        return "spear and bows boas"
    elif spear_boa:
        return "spear bom"
    elif espada_boa:
        return "sword boa"
    else:
        return "arco bom"
    
if __name__ == "__main__":
    print(final_battle())
    

# # 12. A Batalha Final
# # a. Descrição: Um herói precisa decidir qual arma usar na batalha final. Ele tem três armas: uma
# # espada, um arco e uma lança. Cada arma tem um poder de ataque e uma durabilidade. A
# # escolha deve considerar que o poder de ataque seja maior que 50 e a durabilidade maior que
# # 70. Crie um programa que receba os valores de ataque e durabilidade das três armas e
# # determine qual é a mais adequada. Se nenhuma atender, o programa deve sugerir que o herói
# # busque uma nova arma.
# # b. Conceito: Operadores lógicos, relacionais, desvio condicional aninhado.

def final_battle():

    espada_atk = int(input("digite atk: "))
    espada_durability = int(input(("durabilidade")))
    bow_atk = int(input("digite atk: "))
    bow_durability = int(input(("durabilidade")))
    spear_atk = int(input("digite atk: "))
    spear_durability = int(input(("durabilidade")))
    espada_boa,bow_boa,spear_boa = False,False,False
    if espada_atk > 50 and espada_durability >70:
        espada_boa = True

    if bow_atk> 50 and bow_durability >70:
        bow_boa = True

    if spear_atk >50 and spear_durability >70:
        spear_boa = True

    if espada_boa and bow_boa and spear_boa:
        return "AS tres arma sao validas, va com as 3"
    elif espada_boa and bow_boa:
        return "espada e bow boas"
    elif espada_boa and spear_boa:
        return "espada and spear boas"
    elif spear_boa and bow_boa:
        return "spear and bows boas"
    elif spear_boa:
        return "spear bom"
    elif espada_boa:
        return "sword boa"
    else:
        return "arco bom"
    
if __name__ == "__main__":
    print(final_battle())
    
