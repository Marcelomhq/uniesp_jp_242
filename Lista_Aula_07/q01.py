# Calculadora de Média de Notas:
# Contexto: Crie um programa que peça ao usuário para inserir várias 
# notas de um aluno e calcule a média. Utilize um loop para continuar 
# pedindo notas até que o usuário digite um valor específico para 
# encerrar a entrada (por exemplo, -1).
def add_grade():
    i=1
    print(f"Vamos agora adicionar as notas de {aluno}.")
    while True:        
        grade = float(input(f"Digite a nota {i} de {aluno}: "))
        i += 1
        grades.append(grade)
        exit = input("Voce quer adicionar outras nota? s para sim, n para nao: ")
        if exit == 'n':
            break
    return i

def average(grades_list):
    return sum(grades_list)/len(grades_list)

if __name__ == "__main__":
    print("Bem-vindo ao sistemas de notas da Uniesp")
    aluno = input("Digite o nome do aluno: ")
    grades = []
    num_grades = add_grade()
    print(f"A media de {aluno} depois de {num_grades-1} provas foi de: {average(grades)}")
    