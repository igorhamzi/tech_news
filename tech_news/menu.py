import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category)


def options4(options):
    try:
        if options == '6':
            print(top_5_categories())
        elif options == '7':
            print("Encerrando script")
        else:
            sys.stderr.write("Opção inválida\n")
    except ValueError:
        sys.stderr.write(ValueError)


def options3(options):
    try:
        if options == '4':
            input_client = input("Digite a categoria:")
            print(search_by_category(input_client))
        elif options == '5':
            print(top_5_news())
        else:
            options4(options)
    except ValueError:
        sys.stderr.write(ValueError)


def options2(options):
    try:
        if options == '2':
            input_client = input("Digite a data no formato aaaa-mm-dd:")
            print(search_by_date(input_client))
        elif options == '3':
            input_client = input("Digite a tag:")
            print(search_by_tag(input_client))
        else:
            options3(options)
    except ValueError:
        sys.stderr.write(ValueError)


def options1(options):
    try:
        if options == '0':
            input_client = input("Digite quantas notícias serão buscadas:")
            get_tech_news(input_client)
        elif options == '1':
            input_client = input("Digite o título:")
            print(search_by_title(input_client))
        else:
            options2(options)
    except ValueError:
        sys.stderr.write(ValueError)


def analyzer_menu():

    options = input((
        "Selecione uma das opções a seguir:\n 0 - Popular o banco com notícias"
        ";\n 1 - Buscar notícias por título;\n 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n 4 - Buscar notícias por categoria;\n "
        "5 - Listar top 5 notícias;\n 6 - Listar top 5 categorias;\n 7 - Sair."
    ))

    options1(options)
