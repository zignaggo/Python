# Dupla: Alvacy Gonçalves da Fonseca Juniore João Victor Zignago

from scanner import read_string, read_number
from viewer import show_books, show_menu
from controller import add_book, get_books_by_title, add_book_into_reading_books, remove_book_of_reading_books, get_books_by_gender

books = []
reading_books = []
genders = ["autobiografia", "biografia", "conto", "poesia", "romance", "autoajuda"]

while True:
    show_menu("Bem-vindo a Biblioteca", ["Adicionar Livro", "Consultar Livro", "Leitura do momento", "Encerrar programa"])
    option =  read_number("Digite a opção desejada:", 1, 4, "Opção digitada não existe!")
    match option:
        case 4:
            print("Encerrando")
            break
        case 1:
            print("\n[ Adicionar Livro ]")
            title = read_string("Digite o Título do livro: ")
            year = read_number("Digite o ano do livro: ", 1900, 2023, "O ano deve ser entre 1900 e 2023")
            author = read_string("Digite o autor do livro: ")

            # Pegar e validar o gênero
            show_menu("Gêneros", genders)
            index_gender = read_number("Digite a opção desejada:", 1, len(genders), "Opção digitada não existe!")

            add_book(title, year, author, genders[index_gender-1], books)
        case 2:
            show_menu("Livros da Biblioteca", ["Consultar por Título", "Consultar por Gênero"])
            option_books =  read_number("Digite a opção desejada:", 1, 2, "Opção digitada não existe!")
            match option_books:
                case 1:
                    title = read_string("Digite o Título do livro para busca: ")
                    filtered_books = get_books_by_title(title, books)
                    show_books(filtered_books, "Nenhum livro com esse gênero encontrado!")
                case 2:
                    # Pegar e validar o gênero
                    show_menu("Gêneros", genders)
                    index_gender = read_number("Digite a opção desejada:", 1, len(genders), "Opção digitada não existe!")
                    # Mostrar livros filtrados
                    filtered_books = get_books_by_gender(genders[index_gender-1], books)
                    show_books(filtered_books, "Nenhum livro com esse gênero encontrado!")
        case 3:
            show_menu("Leitura do Momento", ["Listar Livros", "Adicionar livro a leitura", "Remover livro da Leitura"])
            option_reading_books =  read_number("Digite a opção desejada:", 1, 3, "Opção digitada não existe!")
            match option_reading_books:
                case 1:
                    print("\n[Leitura do Momento]")
                    show_books(reading_books)
                case 2:
                    print("\n[Leitura do Momento]")
                    show_books(books)
                    number = read_number("Digite o número do livro a ser adicionado: ", 1, len(books), "O indíce digitado não existe!")
                    add_book_into_reading_books(books[number-1][0], reading_books, books)
                case 3:
                    print("\n[Leitura do Momento]")
                    show_books(reading_books)
                    number = read_number("Digite o número do livro a ser adicionado: ", 1, len(books), "O indíce digitado não existe!")
                    remove_book_of_reading_books(books[number-1][0], reading_books)
