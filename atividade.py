import os

produtos = []

def exibirNomePrograma(): 
    print('Sistema de Produtos')

def exibirOpcoes():
    print('1. Cadastrar produto')
    print('2. Listar produto')
    print('3. Alternar estado de um produto')
    print('4. Sair\n')

def escolherOpcao():
    try:
        opcaoEscolhida = int(input('Escolha uma opção: '))
        if opcaoEscolhida == 1: cadastrarProdutos()
        elif opcaoEscolhida == 2: listarProduto()
        elif opcaoEscolhida == 3: alterarProduto()
        elif opcaoEscolhida == 4: finalizar()
        else: opcaoInvalida()
    except:
        opcaoInvalida()

def cadastrarProdutos():
    exibirSubtitulo('Cadastro de novos produtos')
    nomeProduto = input('Digite o nome do produto a ser cadastrado: ')
    categoria = input(f'Digite a categoria do produto {nomeProduto}: ')
    dadosProduto = {'nome':nomeProduto, 'categoria':categoria, 'ativo':False}
    produtos.append(dadosProduto)
    print(f'O produto {nomeProduto} foi cadastrado com sucesso!')
    voltarMenuPrincipal()

def alterarProduto():
    exibirSubtitulo('Alterar estado do produto')
    nomeProduto = input('Digite o nome do produto que deseja alterar o status: ')
    produtoEncontrado = False
    for produto in produtos:
        if nomeProduto == produto['nome']:
            produtoEncontrado = True
            produto['ativo'] = not produto['ativo']
            mensagem = f'O produto {nomeProduto} foi ativado com sucesso' if produto['ativo'] else f'O produto {nomeProduto} foi desativado com sucesso'
            print(mensagem)
    if not produtoEncontrado:
        print('O produto não foi encontrado')
    voltarMenuPrincipal()

def listarProduto():
    exibirSubtitulo('Listagem de produtos')
    print(f'{"Nome do produto".ljust(22)} | {"Categoria".ljust(20)} | Status')
    for produto in produtos:
        nomeProduto = produto['nome']
        categoria = produto['categoria']
        ativo = 'ativado' if produto['ativo'] else 'desativado'
        print(f'- {nomeProduto.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltarMenuPrincipal()

def exibirSubtitulo(subtitulo):
    print(f'\n{subtitulo}\n')

def voltarMenuPrincipal():
    input('\nPressione Enter para voltar ao menu principal...')
    main()

def finalizar():
    print('Obrigado por usar o Sistema de Produtos. Até mais!')

def opcaoInvalida():
    print('Opção inválida. Por favor, escolha uma opção válida.')

def main():
    os.system('cls')
    exibirNomePrograma()
    exibirOpcoes()
    escolherOpcao()

if __name__ == '__main__':
    main()