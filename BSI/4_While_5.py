"""
Q5. Escreva um algoritmo que leia um valor inicial A e imprima a sequência de valores do cálculo de A! e o seu resultado. 
Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120
Utilize o loop while para resolver esta questão.

"""

factorial = int(input("Qual número quer ver o fatorial?: "))
count = factorial
default_string = f"Fatorial de {factorial}! = {factorial}"

while count > 1:
    factorial = factorial * (count-1)
    count -= 1
    default_string += f"x{count}"

print(default_string + " = " + str(factorial))
