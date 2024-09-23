# Escreva um programa em Python que leia o arquivo de texto vingadores.txt e 
# mande uma mensagem convidando-os para uma festa na sua casa.
with open("vingadores.txt","r") as file:
    text = file.read()

list_names = text.split('\n')
for names in list_names:
    print(f"Venha pra minha festa amanha {names}, vai ser bom demais xdd")