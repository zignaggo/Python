# Dupla: Alvacy Gonçalves da Fonseca Juniore João Victor Zignago

def read_number(
        input_message,
        min=0,
        max=None,
        condition_error_message="O número não atende as condições"):

    while True:
        try:
            value = int(input(input_message))
            if value < min or (max and value > max):
                print(f"\n{condition_error_message}")
                continue
            return value
        except ValueError:
            print("\nOcorreu um erro: Apenas números inteiro são aceitos")

def read_string(input_message, error_message="Apenas números inteiro são aceitos"):

    while True:
        try:
            value = str(input(input_message)).strip()
            if not value:
                print("Esse campo é obrigatório")
                continue
            return value
        except ValueError:
            print("\nOcorreu um erro:", error_message)
            return -1
