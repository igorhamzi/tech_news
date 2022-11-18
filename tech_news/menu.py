import sys


def options2(options):

    if options == 3:
        return input("Digite a tag:")
    elif options == 4:
        return input("Digite a categoria:")
    else:
        return sys.stderr.write("Opção inválida")


def options1(options):
    if options == 0:
        return input("Digite quantas notícias serão buscadas:")
    elif options == 1:
        return input("Digite o título:")
    elif options == 2:
        return input("Digite a data no formato aaaa-mm-dd:")
    else:
        return options2(options)


def analyzer_menu():

    options = input((
        "Selecione uma das opções a seguir:\n 0 - Popular o banco com notícias"
        ";\n 1 - Buscar notícias por título;\n 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n 4 - Buscar notícias por categoria;\n "
        "5 - Listar top 5 notícias;\n 6 - Listar top 5 categorias;\n 7 - Sair."
    ))

    return options1(options)
