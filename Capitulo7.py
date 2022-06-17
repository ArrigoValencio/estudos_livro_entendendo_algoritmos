
# Implementando grafo ponderado
grafo = {}
grafo['Partida'] = {}
grafo['Partida']['A'] = 6
grafo['Partida']['B'] = 2
grafo['A'] = {}
grafo['A']['Chegada'] = 1
grafo['B'] = {}
grafo['B']['A'] = 3
grafo['B']['Chegada'] = 5
grafo['Chegada'] = {}

custos = {}
custos['A'] = 6
custos['B'] = 2
custos['Chegada'] = float('inf')

pais = {}
pais['A'] = 'Partida'
pais['B'] = 'Partida'
pais['Chegada'] = None

vertices_processados = []

# Criando função para encontrar vértice de menor custo (será usada dentro do algoritmo)
def vertice_menor_custo (custos):
    menor_custo = float('inf')
    menor_vertice = None
    for vertice in custos:
        custo = custos[vertice]
        if custo < menor_custo and vertice not in vertices_processados:
            menor_custo = custo
            menor_vertice = vertice
    return menor_vertice

    # Algoritmo de Dijkstra
vertice_encontrado = vertice_menor_custo(custos)
while vertice_encontrado is not None:
    vizinhos = grafo[vertice_encontrado]
    custo = custos[vertice_encontrado]
    for vizinho in vizinhos.keys():
        custo_atualizado = custo + vizinhos[vizinho]
        if custo_atualizado < custos[vizinho]:
            custos[vizinho] = custo_atualizado
            pais[vizinho] = vertice_encontrado
    vertices_processados.append(vertice_encontrado)
    vertice_encontrado = vertice_menor_custo(custos)

print(pais)
