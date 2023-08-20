"""

Q4. Em um prédio há 16 apartamentos (1 a 16) e três elevadores (A, B e C). 
Foi realizada uma pesquisa no qual cada apartamento respondia:
O número do apartamento;
O elevador que utiliza com mais frequência;
E o período que em que utiliza mais utiliza este elevador
'M' = matutino
'V' = vespertino
'N' = noturno

Construa um algoritmo que calcula e imprime:
Qual o elevador mais frequentado e em qual período se concentra o maior fluxo;
Qual o período mais usado de todos e a que elevador pertence;

"""
apartament_list = []

schedule_M = []
schedule_V = []
schedule_N = []
most_frequent_schedule = schedule_M
most_frequent_elevator = schedule_M
for index in range(1, 4):
    apto_number = int(input("Número do Apartamento: "))
    elevator = str(input("Qual elevador mais utilizado? (A ou B ou C): ")).upper()
    schedule = str(input("Qual horário mais utilizado? (M ou V ou N): ")).upper()
    apartament_list.append([apto_number, elevator, schedule])

for index, apartament in enumerate(apartament_list):
    if apartament[2] == 'M':
        schedule_M.append(apartament)
    elif apartament[2] == 'V':
        schedule_V.append(apartament)
    elif apartament[2] == 'N':
       schedule_N.append(apartament)

if (len(schedule_V) > len(most_frequent_schedule)):
    most_frequent = schedule_V
if (len(schedule_N) > len(most_frequent_schedule)):
    most_frequent = schedule_N

print('Matutino: ', schedule_M)
print('Vespertino: ', schedule_V)
print('Noturno: ', schedule_N)
print('Mais Frequentado', most_frequent )