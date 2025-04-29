# 3 – Notas de alunos
# Crie um dicionário onde as chaves são nomes de alunos e os valores são listas
# com suas notas. - Calcule a média de cada aluno. - Mostre os alunos com
# # média acima de 7.

alunos = {
    'Ana': [8.5, 7.0, 9.0],
    'Bruno': [6.0, 5.5, 7.0],
    'Carla': [10.0, 9.5, 9.0],
    'Daniel': [4.0, 6.0, 5.5]
}

print("Alunos com média acima de 7:\n")

for aluno, notas in alunos.items():
    media = sum(notas) / len(notas)
    if media > 7:
        print(f'{aluno}: média = {media:.2f}')
