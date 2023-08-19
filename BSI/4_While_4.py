"""
Q4. Escreva um algoritmo que solicita a quantidade de alunos em uma turma de curso de pré-vestibular. 
Depois, solicita que seja informado para cada aluno, se este foi aprovado ou reprovado no vestibular. 
No final, o sistema deverá informar quantos alunos foram aprovados e quantos foram reprovados.
"""

quantity_peaple = int(input("Digite a quantidade de alunos: "))
count = 0
disapproved = 0
approved = 0
while count < quantity_peaple:
    grade = str(input(f"O {count+1}° Aluno foi aprovado? Sim | Não: "))
    if(grade.lower() == "sim"):
        approved += 1
    if (grade.lower() == "nao" or grade.lower() == "não"):
        disapproved += 1
    count += 1
print(f'Foram Aprovados {approved} alunos')
print(f'Foram Reprovados {disapproved} alunos')