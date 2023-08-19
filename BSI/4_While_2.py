"""
Q2. Escreva um algoritmo que leia o nome e a altura de 10 pessoas,
e imprima o nome da maior e da menor pessoa.
"""
"""
# First way
    quantity_peaple = 1
    height = float(input('Qual sua altura?: '))
    taller = height
    smaller = height

    while quantity_peaple < 3:
        height = float(input('Qual sua altura?: '))

        if (height > taller):
            taller = height

        if (height < smaller):
            smaller = height

        quantity_peaple += 1
        
    print(f'Maior: {taller}')
    print(f'Menor: {smaller}')
"""
# Second Way
quantity_peaple = 0

while quantity_peaple < 3:
    height = float(input('Qual sua altura?: '))

    if(quantity_peaple == 0):
        taller = height
        smaller = height

    if (height > taller):
        taller = height

    if (height < smaller):
        smaller = height

    quantity_peaple += 1

print(f'Maior: {taller}')
print(f'Menor: {smaller}')
