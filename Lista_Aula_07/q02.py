# Tabuada Personalizada:
# Contexto: Desenvolva um programa que peça ao usuário um número e 
# gere a tabuada completa desse número (de 1 a 10). Utilize um loop para realizar 
# as multiplicações e exibir os resultados de forma organizada.
def calc_multi_table(number):
    table = []
    for i in range(1,11):
        table.append(num*i)
    return table


if __name__ == "__main__":
    print("Bem-vindo ao programa de tabuadas!")
    num = int(input("Digite o numero desejado para mostrarmos a tabuada ate 10: "))
    multi_table = calc_multi_table(num)
    print(f"Aqui esta a tabuada de {num}")
    for index, n in enumerate(multi_table):
        print(f"{num} vezes {index+1} = {n}")