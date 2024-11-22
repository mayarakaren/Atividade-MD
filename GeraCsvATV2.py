import random
import pandas as pd
from datetime import datetime, timedelta

# Lista de produtos para gerar o nome e id do produto
produtos = [
    (101, "Produto A"),
    (102, "Produto B"),
    (103, "Produto C"),
    (104, "Produto D"),
    (105, "Produto E")
]

# Função para gerar uma data aleatória
def gerar_data_inicial():
    # Define a data inicial (1º de novembro de 2024)
    data_inicial = datetime(2024, 11, 1)
    # Gera uma data aleatória dentro de um intervalo de 30 dias
    data_aleatoria = data_inicial + timedelta(days=random.randint(0, 30))
    return data_aleatoria.strftime('%Y-%m-%d')

# Função para gerar um conjunto de vendas
def gerar_vendas(num_vendas):
    vendas = []
    for id_venda in range(1, num_vendas + 1):
        id_produto, nome_produto = random.choice(produtos)
        quantidade = random.randint(1, 10)  # Quantidade aleatória entre 1 e 10
        preco_unitario = round(random.uniform(5.0, 100.0), 2)  # Preço aleatório entre 5 e 100 reais
        data_venda = gerar_data_inicial()  # Data aleatória no intervalo especificado
        vendas.append([id_venda, id_produto, nome_produto, quantidade, preco_unitario, data_venda])
    return vendas

# Gerar 5000 registros
num_vendas = 5000
vendas = gerar_vendas(num_vendas)

# Criar um DataFrame com os dados gerados
df_vendas = pd.DataFrame(vendas, columns=["id_venda", "id_produto", "nome_produto", "quantidade", "preco_unitario", "data_venda"])

# Salvar o DataFrame como um arquivo CSV
df_vendas.to_csv("vendas_5000_registros.csv", index=False)

print("Arquivo CSV com 5000 registros gerados com sucesso!")
