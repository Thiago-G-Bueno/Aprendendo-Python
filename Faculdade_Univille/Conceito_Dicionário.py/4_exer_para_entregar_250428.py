# Dicionário inicial com alguns produtos
estoque = {
    'camiseta': 10,
    'calça': 5,
    'tênis': 8
}

def adicionar_produto(nome, quantidade):
    if nome in estoque:
        print(f"{nome} já existe. Use a opção de atualizar.")
    else:
        estoque[nome] = quantidade
        print(f"{nome} adicionado com {quantidade} unidades.")

def atualizar_estoque(nome, quantidade):
    if nome in estoque:
        estoque[nome] = quantidade
        print(f"Estoque de {nome} atualizado para {quantidade}.")
    else:
        print(f"{nome} não encontrado no estoque.")

def listar_estoque():
    print("\nEstoque atual:")
    for produto, quantidade in estoque.items():
        print(f"- {produto}: {quantidade} unidades")

def remover_produto(nome):
    if nome in estoque:
        del estoque[nome]
        print(f"{nome} removido do estoque.")
    else:
        print(f"{nome} não encontrado no estoque.")

# Exemplo de uso:
listar_estoque()

adicionar_produto('boné', 12)
atualizar_estoque('camiseta', 15)
remover_produto('calça')

listar_estoque()
