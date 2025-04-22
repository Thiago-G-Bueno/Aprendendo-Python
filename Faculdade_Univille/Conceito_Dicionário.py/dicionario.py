# O que é  uma estrutura que guarda pares de chave e valor 

# Pensa em um dicionário de verdade onde as "chaves" são as
# palavras e o "valor" o significado

aluno = {
    'nome' : 'Maria',
    'idade' : 18,
    'curso' : 'python'
}
# Cria a variável = e aí o colchetes e nome é a chave 
# e Maria é valor

# Forma de como acessar os valores 

print (aluno['nome']) # 'nome' é a chave e o valor  é Maria
print (aluno ['idade']) 
print (aluno['curso']) 

# usando o método .get
# para dizer none ou dizer que é um valor ausente 

print (aluno.get('endereco')) # ira imprimir none, valor ausente 

# como incluir uma chave ao dicionário:

aluno ['matricula'] = 1234 # usamos a classe aluno e criamos a matricula 

print (aluno['matricula'])

# como alterar um valor de uma chave 

aluno ['idade'] = 16 

print (aluno['idade'])

# Remover item do curso 

del aluno ['curso']

print (aluno.get('curso')) 

# Verificar se a chave existe 

if 'idade' in aluno: 
    print (f'{'idade'} está presente em aluno')
else:
    print(f'{'idade'}no está presente me aluno')



