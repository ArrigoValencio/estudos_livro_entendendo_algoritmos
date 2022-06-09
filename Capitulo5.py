
    # Um pouco sobre talbelas hash (em python, dicionários)
# Criando uma função de verificação de votantes
votou = {}
def verifica_eleitor(nome_votante):
    if votou.get(nome_votante):
        print('Já votou, pode ir embora!')
    else:
        votou[nome_votante] = True
        print('Ainda não votou, pode votar!')

# Teste de verificação de eleitor
verifica_eleitor('João')
verifica_eleitor('Maria')
verifica_eleitor('Maria')
