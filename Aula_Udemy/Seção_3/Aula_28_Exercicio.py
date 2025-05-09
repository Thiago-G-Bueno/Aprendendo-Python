"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print('Seu nome é %s ' % (nome))  # Interpolação com %
    print(f'Seu nome é {nome}')       # f-string
    print(nome[::-1])                 # Nome invertido

    # Verificando se o nome contém espaço
    if ' ' in nome:
        print('O nome contém espaço')
    else:
        print('O nome não contém espaço')

    print(len(nome))                          # Tamanho do nome
    print('A primeira letra do seu nome é', nome[0])  # Primeira letra
    print('A última letra do seu nome é', nome[-1])   # Última letra
else:
    print('Você não digitou nada')










