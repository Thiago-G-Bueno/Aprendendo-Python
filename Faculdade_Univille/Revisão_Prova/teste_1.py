# Define uma função para coletar 5 números digitados pelo usuário
def coletar_numeros():
    numeros = []  # Cria uma lista vazia para armazenar os números
    print("Digite 5 números:")  # Informa o usuário o que fazer

    # Usa um laço for para repetir 5 vezes (de 0 a 4)
    for i in range(5):
        # Pede ao usuário para digitar um número e converte para inteiro
        numero = int(input(f"Digite o {i+1}º número: "))
        # Adiciona o número digitado à lista
        numeros.append(numero)

    # Retorna a lista completa com os 5 números
    return numeros

# Define uma função que procura um número dentro de uma lista
def procurar_numero(lista):
    # Pede ao usuário um número a ser procurado e converte para inteiro
    procurado = int(input("Qual número você deseja procurar? "))

    # Verifica se o número procurado está presente na lista
    if procurado in lista:
        # Se estiver na lista, mostra uma mensagem positiva
        print(f"O número {procurado} está na lista.")
    else:
        # Se não estiver, mostra uma mensagem negativa
        print(f"O número {procurado} NÃO está na lista.")

# Parte principal do programa
# Chama a função para coletar os números e armazena o resultado em 'lista_numeros'
lista_numeros = coletar_numeros()

# Chama a função para procurar um número na lista criada
procurar_numero(lista_numeros)
