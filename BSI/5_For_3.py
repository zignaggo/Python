"""
Q3. (WHILE, FOR e LISTAS) Elabore um algoritmo entra em loop solicitando um número inteiro, 
e só para de pedir um novo número quando for digitado um número negativo. 
Para cada número inteiro positivo digitado, deve deverificar se este número é ou não um número primo (um número primo é aquele que é divisível somente por ele mesmo e por 1. O número um por sí só já é primo). Ao final, o programa deve informar:
A quantidade e os números digitados que são primos.
A quantidade e os números digitados que não são primos.

"""
primes = 0
not_primes = 0

while True:
    divisors = 0
    number = int(input('Digite um número ∈ N, (para sair digite um número negativo): '))
    if(number < 0):
        break
    for index in range(1,10):
        if(number % index == 0):
            divisors += 1
    if(divisors > 2):
        not_primes += 1
    else: 
        primes += 1
    


print('Primos: ', primes)
print('Não primos: ', not_primes)


