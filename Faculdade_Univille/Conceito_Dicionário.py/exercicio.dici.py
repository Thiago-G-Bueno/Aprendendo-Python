# Criando o dicionário com dois contatos iniciais
contatos = {
    'Ana': '1234-5678',
    'Bruno': '9876-5432'
}

# Adicionando um novo contato
contatos['Carlos'] = '5555-0000'

# Removendo um contato existente
del contatos['Bruno']

# Atualizando o número de telefone de um contato
contatos['Ana'] = '1111-2222'

# Verificando se um nome está presente na agenda
nome = 'Carlos'
if nome in contatos:
    print(f'{nome} está na agenda com o número {contatos[nome]}')
else:
    print(f'{nome} não está na agenda.')

# Exibindo todos os contatos
print('\nLista de contatos atualizada:')
for nome, telefone in contatos.items():
    print(f'{nome}: {telefone}')
///teste 
