# Programa principal
# José Menescal Neto
# 31/07/2024

from ex115.lib.arquivo import *
from time import sleep

arq = 'cadClientes.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Listar', 'Cadastrar', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de ler o arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar nova pessoa
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do Sistema ... Até logo.')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(2)
