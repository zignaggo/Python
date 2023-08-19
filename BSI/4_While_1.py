"""
Q1. Elabore um algoritmo que efetue a soma de todos os números ímpares 
que são múltiplos de três e que se encontram no conjunto dos números de 1 até 500.
No final, exiba a quantidade de números ímpares múltiplos de 3, e o resultado da soma.
"""

number = 0
count = 0
amount = 0

while number <= 500:
    if number % 3 == 0 and number % 2 != 0:
        amount += number
        count += 1
    number += 1
    
print(f"Soma dos números ímpares: {amount}")
print(f"Quantidade dos números ímpares: {count}")