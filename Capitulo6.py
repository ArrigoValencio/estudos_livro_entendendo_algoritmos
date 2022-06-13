
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
