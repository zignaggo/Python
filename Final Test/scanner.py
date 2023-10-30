"""Module providing a function to read values."""

def read_option(
        input_message,
        min=0,
        max=99999,
        error_message="Fora do limite máximo ou mínimo de opções"):
    """Read Menu Option"""
    
    while True:
        try:
            value = read_number(input_message)
            if value < min or value > max:
                print(error_message)
                continue
            return value
        except ValueError as error:
            print("\nOcorreu um erro:", error)
            return -1


def read_number(
        input_message,
        condition=lambda a: 0 <= a >= 0,
        condition_error_message="O número não atende as condições"):
    """Read int value"""
    while True:
        try:
            value = int(input(input_message))
            if not condition(value):
                print(condition_error_message)
                continue
            return value
        except ValueError:
            print("\nOcorreu um erro: Apenas números inteiro são aceitos")
            return -1


def read_string(input_message, error_message="Apenas números inteiro são aceitos"):
    """Read int value"""
    while True:
        try:
            value = str(input(input_message))
            if not isinstance(value, str):
                print("Apenas letras são aceitas")
                continue
            return value
        except ValueError:
            print("\nOcorreu um erro:", error_message)
            return -1

