## Analytics
- Agrupado pelo departamento e período:

  - Foi extraído o top 10 itens mais relevantes a partir da **contagem distinta de tickets**, pois é a métrica que mais reflete nossa premissa que é vender mais a partir de combos promocionais.

  - A partir desse top 10:

    - Foi extraído o top 15 itens que acompanham cada um dos itens acima.
  
      - Foi criado um *for* que acessa cada um dos itens acima e extrai a lista de tickets de cada um

      - A base foi filtrada a partir da lista acima a fim de extrair o top 15 daquele produto, ou seja, dos tickets que contém aquele produto

      - A base final consiste em uma base de 2 colunas e 150 linhas (15 itens para cada um dos 10), onde a primeira coluna é o item referência do top 10 e a segunda coluna o item relacionado à ela.

- **Código:**
- **Dashboard:**

## Data Science
- Entendendo que a ideia é criar combos promocionais para auxiliar os times comerciais, foi criado dentro do for um algoritmo iterativo que executa para cada um dos departamentos
  - É importante mencionar que essa segmentação por departamento vem muito da ideia de que não estamos organizando itens em uma prateleira de mercado (onde a gente pode pôr a cerveja do lado de uma fralda), ou seja, segmentar nesse caso seria uma péssima ideia, pois limitaria a base.

- **Código:**
- **Relatório:**

## Airflow DAG

- **Código:**
- **Solução item b:**
