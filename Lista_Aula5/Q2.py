# 2. Guerreiro da Idade Média
# a. Descrição: Um guerreiro precisa de uma armadura especial para a batalha. Para forjar a
# armadura, ele precisa de uma liga metálica que combina ferro e ouro. O ferreiro diz que a liga
# precisa ter no mínimo 70% de ferro. Crie um programa que receba a quantidade de ferro e
# ouro em kg e verifique se a porcentagem de ferro na liga é suficiente.
# b. Conceito: Operadores aritméticos, operadores lógicos, desvio condicional simples.

def armadura():
    qtd_ferro = float(input("Digite a quantidade de ferro da sua armadura: "))
    qtd_ouro = float(input("Digite a quantidade de ouro da sua armadura: "))

    if (qtd_ferro/(qtd_ferro+qtd_ouro)) > 0.7:
        return ("Sua armadura tem uma liga resistente o suficiente.")
    else:
        return("Sua armadura nao tem uma liga resistente o suficiente.")

    


if __name__ == "__main__":
    print("Iniciando Arquivo")
    print(armadura())
    print("Finalizando Arquivo")