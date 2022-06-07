
    # Algorítmo Ordenação por Seleção: organizando uma lista do menor para o maior valor
# Criação de função para buscar o elemento de menor valor
def busca_menor(lista):
    menor_valor = lista[0]
    indice_menor_valor = 0
    for i in range(1, len(lista)):
       if lista[i] < menor_valor:
           menor_valor = lista[i]
           indice_menor_valor = i
    return indice_menor_valor

# Escrevendo o algorítmo de Ordenação por Seleção propriamente dito (dentro dele utiliza-se da função criada anteriormente)
def ordenacao_selecao(lista):
    nova_lista = []
    for i in range(len(lista)):
        nova_lista.append(lista.pop(busca_menor(lista)))
    return nova_lista

    # Testando o algorítmo Ordenção por Seleção (ordenação crescente)
minha_lista = [5, 3, 6, 2, 10]

print(ordenacao_selecao(minha_lista))

    # Determinando tempo de execução para o algorítmo Ordenação por Seleção com n = 100 (notação 'Big O')
minha_lista2 = range(1, 101)
n = len(minha_lista2)

tempo_execucao = n ** 2
print(tempo_execucao)

    # Escreveno algorítmo de Ordenação por Seleção do maior para o menor valor (isto não está no capítulo,
    #portanto se constitui em um avanço em relação ao conteúdo original)
# Criação de função para buscar o elemento de maior valor
def busca_maior(lista):
    maior_valor = lista[0]
    indice_maior_valor = 0
    for i in range(1, len(lista)):
       if lista[i] > maior_valor:
           maior_valor = lista[i]
           indice_maior_valor = i
    return indice_maior_valor

# Escrevendo o algorítmo de Ordenação por Seleção propriamente dito (dentro dele também utiliza-se da função criada anteriormente)
def ordenacao_selecao2(lista):
    nova_lista = []
    for i in range(len(lista)):
        nova_lista.append(lista.pop(busca_maior(lista)))
    return nova_lista

# Testando o algorítmo Ordenção por Seleção (ordenação decrescente)
minha_lista = [5, 3, 6, 2, 10]

print(ordenacao_selecao2(minha_lista))

