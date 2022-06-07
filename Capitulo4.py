# algoritmo que soma números de uma lista
def soma(lista):
    # caso base
    if lista == []:
        return 0
    # caso recursivo
    else:
         return  lista.pop(0) + soma(lista)

# testando
minha_lista = [1, 2, 3, 3]
print(soma(minha_lista))

# algorítmo que conta número de ítens de uma lista
def contador(lista):
    # caso base
    if lista == []:
        return 0
    # caso recursivo
    else:
        return len([lista.pop()]) + contador(lista)

# Testando
minha_lista2 = [1,0,2,3,0,5]
print(contador(minha_lista2))

# algorítmo que encontra o valor mais alto em uma lista
def maior_valor(lista):
    if lista == []:
        return None
    else:
        maior = lista[0]
        if maior >= lista[1]:
            lista.pop(1)
        else:
            maior = lista[1]
            lista.pop(0)
        if len(lista) == 1:
            return maior
        else:
            return maior_valor(lista)

# Testando
minha_lista3 = [1,3,4,5,1004,99,104,100,875]
print(maior_valor(minha_lista3))

# algorítmo de pesquisa usando recursão
def pesquisa_indice(lista, item):
    if lista == []:
        return None
    # caso base
    indice_item = 0
    if lista[0] == item:
        return indice_item
    # caso recursivo
    else:
        lista.pop(0)
        return 1 + pesquisa_indice(lista, item)

# Testando
minha_lista4 = [1,3,4,5,1004,99]
print(pesquisa_indice(minha_lista4, 99))

