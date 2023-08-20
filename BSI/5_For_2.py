"""
Q2. (FOR e LISTAS) Elabore um algoritmo que pergunta a quantidade de alunos que a turma possui. 
Depois individualmente solicita as suas 4 médias bimestrais. Após, calcule a média de cada aluno. 
Ao final:
1- Informe quantos alunos foram aprovados, e quantos foram reprovados, sabendo que para ser aprovado, 
o aluno deve atingir no mínimio 6 na média final.
2- Informe a maior, e a menor média.

"""
# Variables
number_students = int(input('Quantos alunos sua turma possui?: '))
student_list = []
higher_average = 0
lower_average = 0
approved = 0
disapproved = 0

for student in range(1, number_students+1):
    student_average = 0

    for semester in range(1, 5):
        grade = float(
            input(f"Quanto o {student}° Aluno tirou no {semester} Bimestre?: "))
        student_average += grade
       
    student_list.append(student_average/4)

    if((student_average/4) < 6):
        disapproved += 1
    else:
        approved += 1

    print('-'*30)

    higher_average = student_list[0]
    lower_average = student_list[0]
    # Get Lower and Higher Average
    for student in student_list:
        if (student > higher_average):
            higher_average = student
        if (student < lower_average):
            lower_average = student

print('Médias: ',student_list)
print('Maior Média: ', higher_average)
print('Menor Média: ', lower_average)
print('Aprovados: ', approved)
print('Reprovados: ', disapproved)
