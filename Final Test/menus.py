def show_menu_time_conversion():
    """Show Menu"""
    print("""\n[1]: Segundos(s) => Minutos(m)
[2]: Minutos(m)  => Segundos(s)
[3]: Minutos(m)  => Horas(h)
[4]: Horas(h)    => Minutos(m)
[5]: Sair""")


def show_menu_market():
    """Show Menu Market"""
    print('\n|-Mercadão do Jaça-|')
    print("""[1]: Vender Produtos
[2]: Mostrar Carrinho de Compras
[3]: Remover produto do carrinho
[4]: Fechar venda
[5]: Relatório
[6]: Sair""")

def show_menu_sell_product(products):
    """Show Menu Sell Product"""
    print('\n|-Produtos-|')
    for index, product in enumerate(products):
        print(f"({index}) - Nome: {product[0]} | Preço: {product[1]}")

def show_menu_shopping_cart(items):
    """Show Menu Sell Product"""
    print('\n|-Carrinho de Compra-|')
    if len(items) == 0:
        print("!!Nenhum item Adicionado!!")
    else:
        for index, item in enumerate(items):
            print(f"({index}) - Nome: {item[0]} | Quantidade: {item[2]} | Total: (unitário: R${item[1]}) R${item[1] * item[2]:.2f}")
