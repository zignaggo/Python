"""
Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
O programa vai perguntar o  valor da casa ,  Salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal sabendo que ela não vai poder exceder 30% do salário  ou então o empréstimo será negado.
"""

valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite seu salário: "))
tempo_anual = float(input("Em quanto tempo deseja pagar? (em anos, ex: 1): "))

parcelas = valor_casa / (tempo_anual * 12)

if (parcelas > salario * 0.3):
    print("empréstimo negado")

print(f"Valor da parcela:R${parcelas:.2f}")
