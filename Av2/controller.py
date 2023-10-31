# Dupla: Alvacy Gonçalves da Fonseca Juniore João Victor Zignago

def get_book_by_title(title: str,  books: list):
    for book in books:
        if title.lower() == book[0].lower():
            return book
    return None


def get_books_by_title(title: str,  books: list):
    filtered_books = []
    for book in books:
        if title.lower() in book[0].lower():
            filtered_books.append(book)
    return filtered_books


def get_books_by_gender(gender: str, books: list):
    filtered_books = []
    for book in books:
        if gender.lower() == book[3].lower():
            filtered_books.append(book)
    return filtered_books


def add_book(title: str, year: int, author: str, gender: str, books: list):
    if not get_book_by_title(title, books):
        books.append([title, year, author, gender])
        print("Livro adicionado com sucesso!")
    else:
        print("Não foi possível adicionar o livro: livro já existente")


def add_book_into_reading_books(title: str, reading_books, books):
    if not get_book_by_title(title, books):
        print("Esse livro não existe na biblioteca")
        return None
    if len(reading_books) > 2:
        print("Máximo de 3 livros na leitura atingido!")
        return None
    if get_book_by_title(title, reading_books):
        print("Esse livro já foi adicionado!")
        return None

    book = get_book_by_title(title, books)
    reading_books.append(book)
    print("Livro adicionado a Lista!")


def remove_book(title, books):
    book = get_book_by_title(title, books)
    for book in books:
        if title == book[0]:
            books.remove(book)


def remove_book_of_reading_books(title, reading_books):
    if get_book_by_title(title, reading_books):
        remove_book(title, reading_books)
        print("Livro removido")
    else:
        print("Livro não encontrado")
