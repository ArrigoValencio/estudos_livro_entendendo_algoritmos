
    # Algorítmo Pesquisa-Binária
def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto)//2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1

    return None

    #Testando o algorítmo Pesquisa-Binária
minha_lista = [1, 3, 5, 7, 9]

print(pesquisa_binaria(minha_lista, 3))
print(pesquisa_binaria(minha_lista, -1))

    # Determinando tempo de execução para o algorítmo Pesquisa-Binária com n = 100 (notação 'Big O')
minha_lista2 = range(1, 101)
n = len(minha_lista2)

import math
tempo_execucao = math.log2(n)
print(tempo_execucao)







