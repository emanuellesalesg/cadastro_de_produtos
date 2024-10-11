from classes.Produto import Produto


def menu():
    print()
    print("1.  Listar Produtos")
    print("2.  Inserir Produtos")
    print("3.  Alterar Produtos")
    print("4.  Excluir Produtos")
    print("0.  Sair")
    print()

opcao = 1
while opcao != 0:

    menu()
    opcao = int(input('Escolha uma opção: '))

    match opcao:
        case 1:
            Produto.listarTodos()
        case 2:
            codigo = input('Código: ')
            nome = input('Nome: ')
            quantidade = input('Quantidade: ')
            valor = input('Valor: ')

            produto = Produto(codigo, nome, quantidade, valor)
            produto.inserir()
        case 3:
            Produto.listarTodos()

            selecionado = int(input('Qual item deseja alterar? '))

            item = Produto.consultar(selecionado)

            quantidade = int(input('Quantidade: '))

            valor = int(input('Valor: '))

            produto = Produto(item['codigo'], item['nome'], quantidade, valor)

            produto.alterar(selecionado)
        case 4:
            Produto.listarTodos()
            selecionado = int(input('Qual item deseja excluir? '))
            Produto.excluir(selecionado)
        

