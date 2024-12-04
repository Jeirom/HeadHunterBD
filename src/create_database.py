import psycopg2
from src.api_headhunter import HeadHunterAPI
from config import config


class DBConnector:


    params = {'host': 'localhost',
              'user': 'postgres',
              'password': 123456789,
              'port': 5432,
              'client_encoding': 'utf=8'}
    @staticmethod
    def create_database(database_name: str, params: dict):
        """Создание базы данных и таблиц для сохранения данных о компаниях и их вакансии."""

        conn = psycopg2.connect(dbname='postgres', **params) #Подключаемся к БД с параметрами переменной params
        conn.autocommit = True #Делаем автокоммит
        cur = conn.cursor()

        # try:
        #     cur.execute(f"DROP DATABASE {database_name}")
        # except Exception as e:
        #     print(f'Информация: {e}')
        # # else:
        #  # Исключений не произошло, БД дропнута
        # finally:
        #     cur.execute(f"CREATE DATABASE {database_name}")

        cur.execute(f"DROP DATABASE {database_name}")
        cur.execute(f"CREATE DATABASE {database_name}")
        # result = HeadHunterAPI.filter_name_company()
        with psycopg2.connect(dbname=database_name, **params) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE company( 
                        id_company SERIAL PRIMARY KEY,
                        name_company VARCHAR(255) NOT NULL,
                        company_url TEXT
                        )
                """)

            with conn.cursor() as cur:
                cur.execute(""" CREATE TABLE vacancy(
                        vacancy_id SERIAL PRIMARY KEY,
                        id_company INTEGER REFERENCES company(id_company),
                        url TEXT,
                        salary INTEGER DEFAULT 0
                        )""")

            conn.commit()
            cur.close()


    @staticmethod
    def connect_to_db(query, params=params):
        conn = psycopg2.connect(dbname='postgres', **params)
        cur = conn.cursor()
        conn.autocommit = True
        cur.execute(query, params)
        result = cur.fetchall()
        return result

params = {'host': 'localhost',
          'user': 'postgres',
          'password': 123456789,
          'port': 5432,
          'client_encoding': 'utf=8'}
print(DBConnector.create_database('new', params))