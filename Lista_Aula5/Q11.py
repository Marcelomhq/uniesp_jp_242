# 11. Decisão da Coroa Real
# a. Descrição: O conselho real precisa tomar uma decisão crítica: 
# selecionar o próximo
# governante entre três candidatos, baseado na sua pontuação em uma série 
# de provas. Crie um programa que receba as notas dos três candidatos e 
# determine qual deles teve a maior média.
# Caso duas ou mais médias sejam iguais, o programa deve exibir uma 
# mensagem informando que há um empate.
# b. Conceito: Operadores aritméticos, relacionais, desvio condicional aninhado.

def decision(c1n1,c1n2,c2n1,c2n2,c3n1,c3n2):
    media1 = (c1n1+c1n2)/2
    media2 = (c2n1+c2n2)/2
    media3 = (c3n1+c3n2)/2
    max_media = max (media1,media2,media3)
    
    #Check if theres a draw
    results = []
    if media1 == max_media:
        results.append(f"Constante 1 com a media de {media1:.2f}")
    if media2 == max_media:
        results.append(f"Constante 2 com a media de {media2:.2f}")
    if media3 == max_media:
        results.append(f"Constante 3 com a media de {media3:.2f}")
    
    if len(results) == 1:
        return f"O contestante com a maior media foi o {results[0]}"
    else:
        return f"Houve um empate! Os contestantes com a maior media foram: {', '.join(results)}"
    
    

if __name__ == "__main__":
    print("Bem vindo a decisao do rei!!!")
    cont1_nota1 = float(input("Contestante 1: Qual foi sua nota na primeira prova? "))
    cont1_nota2 = float(input("Contestante 1: Qual foi sua nota na segunda prova? "))
    cont2_nota1 = float(input("Contestante 2: Qual foi sua nota na primeira prova? "))
    cont2_nota2 = float(input("Contestante 2: Qual foi sua nota na segunda prova? "))
    cont3_nota1 = float(input("Contestante 3: Qual foi sua nota na primeira prova? "))
    cont3_nota2 = float(input("Contestante 3: Qual foi sua nota na segunda prova? "))
    print(decision(cont1_nota1,cont1_nota2,cont2_nota1, cont2_nota2, cont3_nota1, cont3_nota2))
