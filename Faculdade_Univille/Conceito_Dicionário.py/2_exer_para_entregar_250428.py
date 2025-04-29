# 2 - Contagem de frequência
# Faça um programa que peça ao usuário para digitar uma palavra e mostre um
# dicionário com a frequência de cada letra.
# Exemplo: Para a palavra 'banana', a saída será {'b': 1, 'a': 3, 'n': 2}

palavra = input("Digite uma palavra: ")

frequencia = {}

for letra in palavra:
    if letra in frequencia:
        frequencia[letra] += 1
    else:
        frequencia[letra] = 1

print(frequencia)
