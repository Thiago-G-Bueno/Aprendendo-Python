
# # Criando o dicionário com dois contatos iniciais
# contatos = {
#     'Ana': '1234-5678',
#     'Bruno': '9876-5432'
# }

# # Adicionando um novo contato
# contatos['Carlos'] = '5555-0000'

# # Removendo um contato existente
# del contatos['Bruno']

# # Atualizando o número de telefone de um contato
# contatos['Ana'] = '1111-2222'

# # Verificando se um nome está presente na agenda
# nome = 'Carlos'
# if nome in contatos:
#     print(f'{nome} está na agenda com o número {contatos[nome]}')
# else:
#     print(f'{nome} não está na agenda.')

# # Exibindo todos os contatos
# print('\nLista de contatos atualizada:')
# for nome, telefone in contatos.items():
#     print(f'{nome}: {telefone}')



# 1 – Dicionário de contatos
# Crie um dicionário chamado contatos com pelo menos dois nomes e seus
# respectivos telefones.
# - Adicione um novo contato.
# - Remova um contato existente.
# - Atualize o número de telefone de um contato.
# - Verifique se um nome está presente na agenda.

# 1 criando a variavel que ira se chamar contato que 
# irá armazenar as chaves e valores 

contato = {
    'joao':'9999-8888', #não esqueça das virgulas 
    'carlos':'2222-3333',
    'davi':'4231-4123'
}

for nome in contato:
    print(f"{nome}: {contato[nome]}")


