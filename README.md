## Analytics
- Agrupado pelo departamento e período:

  - Foi extraído o top 10 itens mais relevantes a partir da **contagem distinta de tickets**, pois é a métrica que mais reflete nossa premissa que é vender mais a partir de combos promocionais.

  - A partir desse top 10:

    - Foi extraído o top 15 itens que acompanham cada um dos itens acima.
  
      - Foi criado um *for* que acessa cada um dos itens acima e extrai a lista de tickets de cada um

      - A base foi filtrada a partir da lista acima a fim de extrair o top 15 daquele produto, ou seja, dos tickets que contém aquele produto

      - A base final consiste em uma base de 2 colunas e 150 linhas (15 itens para cada um dos 10), onde a primeira coluna é o item referência do top 10 e a segunda coluna o item relacionado à ela.

- **Código:** https://github.com/Leolupe/case-sams-club/blob/main/analytics.ipynb
- **Dashboard:** https://public.tableau.com/views/samsclub_OnePage/OnePage?:language=pt-BR&publish=yes&:sid=&:display_count=n&:origin=viz_share_link

## Data Science
- Entendendo que a ideia é criar combos promocionais para auxiliar os times comerciais, foi criado dentro do for um algoritmo iterativo que executa para cada um dos departamentos

   - É importante mencionar que essa segmentação por departamento vem muito da ideia de que não estamos organizando itens em uma prateleira de mercado (onde a gente pode pôr a cerveja do lado de uma fralda), ou seja, segmentar nesse caso seria uma péssima ideia, pois limitaria a base.
 
- Foi feito um for que roda para cada departamento

- Foi feito um pivot da base onde o índice é o ticket e as colunas os produtos em questão, tratados com dummies (0 ou 1) para compra ou não compra do item na transação.

- Foi aplicado o algoritmo fpgrowth que lidou bem com o formato e tamanho da base.

   - O min_support definido foi 0,1%, ou seja, para cada combo considerado, precisamos ter a aparição dos mesmos pelo menos 0,1% das transações (foi parâmetro que trouxe mais variedade de combos, mas poderia ser feito um tuning ou ficaria a depender muito da regra de negócio).
   
   - O min_threshold definido foi 80%.

- O resultado foi uma base contendo cada uma das combinações encontradas, com as métricas do algoritmo e o departamento em questão.

- No relatório, é possível cada departamento explorar as combinações mais atrativas de produtos e a métrica que ilustre a importância da associação.

- **Código:** https://github.com/Leolupe/case-sams-club/blob/main/product_association.py
- **Relatório:** https://public.tableau.com/views/samsclub_Analytics/Analytics?:language=pt-BR&publish=yes&:sid=&:display_count=n&:origin=viz_share_link

## Airflow DAG

- Foram importadas as biblioteca necessárias
- Foram configurados os argumentos principais da dag (tentativas, delay, data de início de periodicidade da atualização com o cron)
- Foi parametrizado a data da execução e com isso a extração d-3
- Foram configuradas as rotinas da query Q1 e a execução do algoritmo de ML

- **Código:** https://github.com/Leolupe/case-sams-club/blob/main/dag.py
- **Solução item b:**
  - Para gravar a saída do algoritmo ML em uma tabela do BigQuery, poderíamos adicionar nova tarefa __BigQueryOperator_ após a tarefa _PythonOperator_, para carregar os dados resultantes do script para uma tabela no BigQuery.
