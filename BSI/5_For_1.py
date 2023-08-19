"""
Elabore um algoritmo que simule uma tabuada
"""
# First Way

for number in range(1, 11):
    print('-'*17)
    print(f"| Tabuada do {number} |")
    print('-'*17 )
    for mutiplier in range(1, 11):
        print(f"| {number} x {mutiplier} = {number*mutiplier}")

