
    # Exemplificação de recursão (função recursiva)
# Contagem regressiva
def contagem_regressiva(x):
    print(x)
    # caso base
    if x <= 1:
        return
    # caso recursivo
    else:
        contagem_regressiva(x - 1)

print(contagem_regressiva(5))

# Cálculo fatorial de um número
def fatorial(y):
    # caso base
    if y == 1:
        return 1
    # caso recursivo
    else:
        return y * fatorial(y-1)

print(fatorial(3))

