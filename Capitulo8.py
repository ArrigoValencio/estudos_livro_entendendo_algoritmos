    #Algoritmo de aproximação
# Exemplo com estações de rádio que abranjam maior número de estados
# Estados a serem abrangidos
estados_abranger = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

# Estações de rádio e estados abrangidos por elas
estacoes = {}
estacoes['kum'] = set(['id', 'nv', 'ut'])
estacoes['kdois'] = set(['wa', 'id', 'mt'])
estacoes['ktres'] = set(['or', 'nv', 'ca'])
estacoes['kquatro'] = set(['nv', 'ut'])
estacoes['kcinco'] = set(['ca', 'az'])

estacoes_finais = set()

while estados_abranger:
    melhor_estacao = None
    estados_cobertos = set()
    for estacao, estados in estacoes.items():
        cobertos = estados_abranger & estados
        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = estados
    estados_abranger -= estados_cobertos
    estacoes_finais.add(melhor_estacao)

print(estacoes_finais)


