import pandas as pd
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules

# Ler os dados do arquivo CSV para um DataFrame
df = pd.read_csv('CASE_PRATICO_SAMS_CLUB.csv')
df = df[~df['item_descricao'].str.contains('SACOLA', case=False)] # removendo o item sacola

# Filtrar os departamentos únicos
departamentos = df['departamento'].unique()

# Lista para armazenar as regras de associação de cada departamento
todas_regras = []

# Iterar sobre os diferentes departamentos
for departamento in departamentos:
    # Filtrar o DataFrame para incluir apenas o departamento atual
    df_departamento = df[df['departamento'] == departamento]
    
    # Criar uma matriz de cesta usando pivot_table para este departamento
    basket = df_departamento.pivot_table(index='ticket', columns='item_descricao', aggfunc='size', fill_value=0)
    basket = basket.applymap(lambda x: 1 if x > 0 else 0)
    
    # Aplicar o FP-Growth para encontrar itens frequentes de tamanho 3
    frequent_itemsets = fpgrowth(basket, min_support=0.001, use_colnames=True)
    
    # Gerar as regras de associação
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=0.8)
    
    # Adicionar uma coluna indicando o departamento
    rules['departamento'] = departamento
    
    # Adicionar as regras deste departamento a lista de todas as regras
    todas_regras.append(rules)

regras_completas = pd.concat(todas_regras)

regras_completas.sort_values(by='support', ascending=False)
regras_completas.to_excel('outputs/regras_combo_ml.xlsx', index=False)
regras_completas