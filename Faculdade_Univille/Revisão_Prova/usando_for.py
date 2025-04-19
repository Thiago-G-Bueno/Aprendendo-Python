numeros = []  # Lista global

def somar_lista():
    total = 0
    for n in numeros:
        total += n
    return total

# Vamos usar o for para repetir 100 vezes no máximo, por exemplo
for i in range(100):
    n = int(input("Digite um número (0 para sair): "))
    if n == 0:
        break
    numeros.append(n)

print("Soma total:", somar_lista())
