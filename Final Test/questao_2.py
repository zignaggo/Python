from scanner import read_number, read_option
from menus import show_menu_market, show_menu_sell_product, show_menu_shopping_cart
shopping_cart = []
products = [
    ["Laranja", 12.99],
    ["Pera", 8.99],
    ["Uva", 23.99],
    ["Abacaxi", 15.99],]
extract = []
while True:
    show_menu_market()
    option = read_option("Digite opção desejada: ", 1, 6, "\nOpção não encontrada/Inválida\n")
    match option:
        case 6:
            break
        case 1:
            show_menu_sell_product(products)
            option = read_option("Digite opção desejada: ", 0, len(products)-1, "\nProduto não encontrado\n")
            quantity = read_number("Quantos produtos deseja vender?: ", lambda value: value >= 1, "Quantidade tem que ser maior ou igual a 1")
            selected_product = products[option]
            selected_product.append(quantity)
            shopping_cart.append(selected_product)
        case 2:
            show_menu_shopping_cart(shopping_cart)
        case 3:
            while True:
                show_menu_shopping_cart(shopping_cart)
                if len(shopping_cart) == 0:
                    break
                option = read_option("Qual produto deseja Remover?: ", 0, len(shopping_cart)-1, "\nProduto não encontrado\n")
                shopping_cart.pop(option)
                remove_again = read_option("Ainda deseja remover Produtos? [1] para sim, [2] para não: ", 1, 2, "\nOpção inválida\n")
                if remove_again == 2:
                    break
        case 4:
            if len(shopping_cart) > 0:
                close_sell = read_option("Deseja realmente fechar a venda? [1] para sim, [2] para não: ", 1, 2, "\nOpção inválida\n")
                if close_sell == 1:
                    total_sell = 0
                    for item in shopping_cart:
                        total_sell += item[1] * item[2]
                    extract.append(total_sell)
                    shopping_cart = []
        case 5:
            print("|-Relatório de Vendas-|")
            total_sells = 0
            for index, item in enumerate(extract):
                total_sells += item
                print(f"{index} - Valor: R${item:.2f}")
            print(f"Total das Vendas: {total_sells}")
