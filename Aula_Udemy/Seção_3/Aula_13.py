#Formatação de String 
# f-strings: f"texto{variável}"



nome = 'Thiago'
altura = 1.70
peso = 74
imc = peso/(altura*altura)

print(f"{nome} tem {altura} de altura, seu peso é {peso:.2f} e seu imc é {imc:.2f}")
