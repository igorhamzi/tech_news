import sys


def test2(options):

    if options == 3:
        return input("Digite a tag:")
    elif options == 4:
        return input("Digite a categoria:")
    else:
        return sys.stderr.write("Opção inválida")


def test1(options):
    if options == 0:
        return input("Digite quantas notícias serão buscadas:")
    elif options == 1:
        return input("Digite o título:")
    elif options == 2:
        return input("Digite a data no formato aaaa-mm-dd:")
    else:
        return test2(options)


def analyzer_menu():

    teste = ('''Selecione uma das opções a seguir:
             0 - Popular o banco com notícias;
             1 - Buscar notícias por título;
             2 - Buscar notícias por data;
             3 - Buscar notícias por tag;
             4 - Buscar notícias por categoria;
             5 - Listar top 5 notícias;
             6 - Listar top 5 categorias;
             7 - Sair.''')

    options = input(teste)
    return test1(options)
