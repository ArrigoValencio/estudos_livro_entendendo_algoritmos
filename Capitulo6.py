
    # Implementando um grafo
# Grafos são implementados através da estrutura de dados tabela hash (dicionário)
# Grafo que traduz uma rede de amigos
meu_grafo = {}
meu_grafo['eu'] = ['Alice', 'Bob', 'Claire']
meu_grafo['Bob'] = ['Anuj', 'Peggy']
meu_grafo['Alice'] = ['Peggy']
meu_grafo['Claire'] = ['Jonny', 'Thom']
meu_grafo['Anuj'] = []
meu_grafo['Peggy'] = []
meu_grafo['Jonny'] = []
meu_grafo['Thom'] = []

    # Algoritmo Pesquisa em largura
# Implementando o algoritmo a partir do grafo criado (busca-se um vendedor de mangas na rede de amigos)
from collections import deque
def pesquisa_largura(pessoa):
    # Criando fila
    fila_pesquisa = deque()
    fila_pesquisa += meu_grafo[pessoa]

    # Criando função que defina vendedor de mangas (no caso, se a última letra do nome da pessoa é 'm')
    def e_vendedor_mangas(pessoa_da_rede):
        return pessoa_da_rede[-1] == 'm'
    pessoas_verificadas = []
    while fila_pesquisa:
        pessoa_da_rede = fila_pesquisa.popleft()
        if not pessoa_da_rede in pessoas_verificadas:
            if e_vendedor_mangas(pessoa_da_rede):
                return print(pessoa_da_rede + ' vende mangas.')
            else:
                fila_pesquisa += meu_grafo[pessoa_da_rede]
                pessoas_verificadas.append(pessoa_da_rede)
    return print('Ninguém vende mangas.')

# Testando o algoritmo pesquisa em largura
pesquisa_largura('eu')


