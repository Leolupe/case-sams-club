from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'retries': 3,
    'retry_delay': timedelta(minutes=5), 
    'start_date': datetime(2024, 2, 22),  # Data de inicio ficticia da dag
    'schedule_interval': '0 7 * * 4'  # Cron que executa toda quinta feira as 7
}

dag = DAG(
    'product_association_pipeline',
    default_args=default_args,
    description='Pipeline to execute Q1 query and product_association.py',
)

date_max = '{{ execution_date }}'
date_min = '{{ execution_date - macros.timedelta(days=3) }}' # Rodar para 3 dias atras

# Configurando a rotina da query Q1

q1_query_task = BigQueryExecuteQueryOperator(
    task_id='run_q1_query',
    sql='Q1.sql',  # arquivo da query
    parameters={'date_max': date_max, 'date_min': date_min},
    dag=dag
)

# Funçao para rodar o algoritmo implementado
def run_product_association_script():
    script_path = os.path.join(os.path.dirname(__file__), 'product_association.py')
    os.system(f'python {script_path}')

# Configurando a rotina do código product_association
product_association_task = PythonOperator(
    task_id='run_product_association',
    python_callable=run_product_association_script, # rodando a funcao que importa o script
    dag=dag
)

q1_query_task >> product_association_task # criando dependencia da base origem com o codigo implementado


