from scanner import read_number, read_option
from menus import show_menu_time_conversion
from conversion_time import decrease_time, increase_time

while True:
    show_menu_time_conversion()
    option = read_option("Digite a opção desejada: ", 1, 5)
    match option:
        case 5:
            break
        case 1:
            seconds = read_number("\nDigite os segundos a serem transformado em minutos: ")
            print(f"Transformando {seconds} segundos em minutos ficará {decrease_time(seconds):.2f} minutos\n")
        case 2:
            minutes = read_number("\nDigite os minutos a serem transformado em segundos: ")
            print(f"Transformando {minutes} minutos em segundos ficará {increase_time(minutes):.2f} segundos\n")
        case 3:
            minutes = read_number("\nDigite os minutos a serem transformado em horas: ")
            print(f"Transformando {minutes} minutos em horas ficará {decrease_time(minutes):.2f} hora(s)\n")
        case 4:
            hour = read_number("\nDigite as horas a serem transformado em minutos: ")
            print(f"Transformando {hour} horas em minutos ficará {increase_time(hour):.2f} minutos(s)\n")
