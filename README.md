### **README - Mineração de Dados: Análise de Vendas**

---

#### **Objetivo**

O objetivo deste projeto é realizar a mineração de dados em um conjunto de registros de vendas de produtos. Através da análise dos dados, buscamos identificar os produtos mais vendidos e os que geraram a maior receita, utilizando a biblioteca `pandas` para processamento e `matplotlib` para visualização.

---

#### **Requisitos**

- Python 3.x
- Bibliotecas:
  - `pandas` (para manipulação de dados)
  - `matplotlib` (para visualização gráfica)

Você pode instalar as bibliotecas necessárias usando o seguinte comando:

```bash
pip install pandas matplotlib
```

---

#### **Descrição dos Dados**

O arquivo de dados fornecido contém as seguintes colunas:

- **id_venda**: Identificador único de cada venda.
- **id_produto**: Identificador único de cada produto.
- **nome_produto**: Nome do produto vendido.
- **quantidade**: Quantidade vendida do produto.
- **preco_unitario**: Preço unitário do produto.
- **data_venda**: Data da venda.

---

#### **Etapas da Análise**

1. **Carregar os Dados**  
   O arquivo CSV contendo os registros de vendas é carregado em um DataFrame do `pandas`.

2. **Agrupamento por Produto e Quantidade Vendida**  
   Os dados são agrupados por nome do produto, somando a quantidade vendida de cada um. Em seguida, os produtos são ordenados pela quantidade vendida, da maior para a menor.

3. **Gráfico de Barras - Produtos Mais Vendidos**  
   Um gráfico de barras é gerado para exibir os 10 produtos mais vendidos com base na quantidade.

4. **Cálculo da Receita Gerada por Produto**  
   A receita gerada por cada produto é calculada multiplicando a quantidade vendida pelo preço unitário. Em seguida, os produtos são agrupados por nome e a receita total de cada um é somada.

5. **Gráfico de Barras - Produtos com Maior Receita**  
   Outro gráfico de barras é gerado para mostrar os 10 produtos com maior receita gerada.

---

#### **Como Usar**

1. Faça o download do arquivo `vendas_5000_registros.csv` ou use seu próprio arquivo CSV contendo os dados de vendas.
2. Coloque o arquivo CSV no mesmo diretório que o script Python.
3. Execute o script em um ambiente Python (por exemplo, Jupyter Notebook ou diretamente no terminal):
   ```bash
   python seu_script.py
   ```

4. O script irá gerar dois gráficos de barras:
   - **Top 10 Produtos Mais Vendidos**: Exibindo os produtos com maior quantidade vendida.
   - **Top 10 Produtos com Maior Receita**: Exibindo os produtos com maior receita gerada.

---

#### **Exemplo de Saída Esperada**

- **Gráfico 1**: Top 10 Produtos Mais Vendidos
  - Exibe as quantidades vendidas para os 10 produtos mais vendidos.

- **Gráfico 2**: Top 10 Produtos com Maior Receita
  - Exibe a receita total gerada pelos 10 produtos com maior receita.

---

#### **Conclusão**

Este projeto demonstrou como realizar a mineração de dados em um conjunto de vendas, destacando produtos com base em suas quantidades vendidas e receitas geradas. As visualizações gráficas proporcionaram uma forma clara de entender os principais produtos no portfólio e podem ajudar na tomada de decisões estratégicas para aumentar a eficiência das vendas e o lucro.

---

#### **Licença**

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT).

--- 
