import psycopg2

def create_database(database_name: str, params: dict):
    """Создание базы данных и таблиц для сохранения данных о компаниях и их вакансии."""
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit()
    cur = conn.cursor()

    cur.execude(f'DROP DATABASE {database_name}')
    cur.execude(f'CREATE DATABASE {database_name}')

    conn.close()

    with psycopg2.connect(dbname=database_name, **params) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE company ( #допиши когда узнаешь из чего будет состоять!!!
                    
                )
            """)

        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE vacancy (
                    
                )
            """)

        conn.commit()
        conn.close()
