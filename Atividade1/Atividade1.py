import os

class Pessoa:
    def __init__(self,altura,genero):
        self.altura = altura
        self.genero = genero
    
def informacao(vezes):
    for i in range(vezes):
        genero = input(f'Qual seu genero da pessoa {i+1}?(M/F) ')
        altura = int(input(f'Qual a altura da pessoa {i+1}? '))        
        pessoa = Pessoa(altura,genero)
        listaPessoas.append(pessoa)

listaPessoas = []
listaTemp = []
numFeminino = 0
os.system('cls')

vezes = int(input('Quantas pessoas voce quer adicionar? '))

informacao(vezes)

for i in listaPessoas:
    listaTemp.append(i.altura)

max = max(listaTemp)
min = min(listaTemp)



listaTemp = []
for i in listaPessoas:
    if i.genero == "M" or i.genero == 'm':
        listaTemp.append(i.altura)
    if i.genero == "F" or i.genero == 'f':
        numFeminino += 1 
        

mediaMasculina = sum(listaTemp)/len(listaTemp)

print(f'Altura maxima: {max}.')
print(f'Altura minima: {min}.')
print(f'Media de altura masculino: {mediaMasculina}.')
print(f'Numero de pessoas femininas: {numFeminino}.')


