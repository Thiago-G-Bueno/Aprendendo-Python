#Crie um programa que solicite ao usuário digitar números e armazene-os 
#em uma lista. Pode ser 5 números. Deverá estar em uma função. 
#Depois, crie uma função que pergunte ao usuário qual 
#número deseja procurar e diga se ele está ou não na lista. 
#Use if e else.

def criar_lista (): # criando a função
    numeros = [] # criando uma lista vazia, que ira guardar os 5 números 
    for i in range(5): # criamos esse laço para repetir o pedido do número 5x
        num = int(input(f"Digite o {i+1}º números"))
        numeros.append(num)
    return numeros