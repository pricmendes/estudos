from datetime import datetime, timedelta
from airflow.decorators import dag, task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook


@task
def get_max_primary_key(table_name: str, sf_conn_id: str):


    hook = SnowflakeHook(snowflake_conn_id=sf_conn_id)

    primary_key = f'ID_{table_name}'
    sql = f"SELECT MAX({primary_key}) FROM {table_name}"
    

    result = hook.get_first(sql)
    max_id = result[0] if result and result[0] is not None else 0
    print(f"Max ID na tabela '{table_name}' do Snowflake é: {max_id}")
    return max_id

@task
def load_incremental_data(table_name: str, max_id: int, pg_conn_id: str, sf_conn_id: str):

    pg_hook = PostgresHook(postgres_conn_id=pg_conn_id)
    pg_conn = pg_hook.get_conn()
    
    with pg_conn.cursor() as pg_cursor:
        primary_key = f'ID_{table_name}'
        
        pg_cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}' ORDER BY ordinal_position")
        columns = [row[0] for row in pg_cursor.fetchall()]
        columns_list_str = ', '.join(f'"{c}"' for c in columns)
        
        select_sql = f"SELECT {columns_list_str} FROM {table_name} WHERE {primary_key} > {max_id}"
        pg_cursor.execute(select_sql)
        rows = pg_cursor.fetchall()

        if not rows:
            print(f"Nenhum dado novo para carregar na tabela '{table_name}'.")
            return

        print(f"Encontrados {len(rows)} novos registros para carregar na tabela '{table_name}'.")

        
        sf_hook = SnowflakeHook(snowflake_conn_id=sf_conn_id)
        
        sf_hook.insert_rows(
            table=table_name,
            rows=rows,
            target_fields=columns
        )
        print(f"Carregamento incremental para a tabela '{table_name}' concluído com sucesso.")




@dag(
    dag_id='postgres_to_snowflake_incremental_load',
    default_args={
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2025, 6, 11),
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=2),
    },
    description='Carrega dados incrementalmente do Postgres para o Snowflake para múltiplas tabelas.',
    schedule=timedelta(days=1),
    catchup=False,
    tags=['etl', 'postgres', 'snowflake'],
)
def postgres_to_snowflake_etl():
    

    table_names = ['veiculos', 'estados', 'cidades', 'concessionarias', 'vendedores', 'clientes', 'vendas']


    POSTGRES_CONN_ID = 'postgres'
    SNOWFLAKE_CONN_ID = 'snowflake'
    

    for table in table_names:

        max_id_value = get_max_primary_key.override(task_id=f'get_max_id_{table}')(
            table_name=table, 
            sf_conn_id=SNOWFLAKE_CONN_ID
        )


        load_incremental_data.override(task_id=f'load_data_{table}')(
            table_name=table, 
            max_id=max_id_value,
            pg_conn_id=POSTGRES_CONN_ID,
            sf_conn_id=SNOWFLAKE_CONN_ID
        )


postgres_to_snowflake_etl_dag = postgres_to_snowflake_etl()
