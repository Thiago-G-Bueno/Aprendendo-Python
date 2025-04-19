#2 - Crie uma função que receba uma lista de números como parâmetro e 
#retorne o maior número da lista. 
# No final mostrar qual o maior número da lista. 
#Podem ser 5 números. 
# Use uma estrutura de repetição para percorrer os 
#elementos

numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

maior = numeros[0]  # começa assumindo que o primeiro é o maior

for num in numeros:
    if num > maior:
        maior = num

print("O maior número é:", maior)


