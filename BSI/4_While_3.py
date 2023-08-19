"""
Q3. Escreva um algoritmo que possui um número secreto de 1 a 100, 
e fica pedindo que o usuário digite um número inteiro de 1 a 100 até acertar o número secreto. 
Quando acertar, informar com quantos chutes ele conseguiu acertar o número.
"""
from random import randint
secret_number = randint(1, 10)
user_number = int(input('Em qual número eu pensei?: '))

while secret_number != user_number:
    print('Você errou! Tente Novamente')
    user_number = int(input('Em qual número eu pensei?: '))
    
print(f'Parabéns o número realmente era o {user_number}')