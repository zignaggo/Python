# Dupla: Alvacy Gonçalves da Fonseca Juniore João Victor Zignago
def show_menu(title: str, options: list):
    print(f"\n[-{title}-]")
    for index, option in enumerate(options):
        print(f"[{index+1}] - {option}")

def show_books(books, error_message = "Nenhum livro adicionado!"):
    print("\n[-Livros-]")
    if len(books) > 0:
        for index, book in enumerate(books):
            print(f"{index+1} - Título: {book[0]}; Ano: {book[1]}; Autor: {book[2]}; Gênero: {book[3]}")
    else:
        print(error_message)
