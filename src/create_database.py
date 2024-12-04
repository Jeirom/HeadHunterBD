import os
import psycopg2
from src.api_headhunter import HeadHunterAPI
from config import config
class DBConnector:


    # def __init__(self):
    #     self._host = os.getenv("host")
    #     self._username = os.getenv("user")
    #     self._port = os.getenv("port")
    #     self._password = os.getenv("password")
    params = config()
    @staticmethod
    def create_database(database_name: str, params: dict):
        """Создание базы данных и таблиц для сохранения данных о компаниях и их вакансии."""
        conn = psycopg2.connect(dbname='postgres', **params)
        conn.autocommit()
        cur = conn.cursor()

        try:
            cur.execute(f"DROP DATABASE {database_name}")
        except Exception as e:
            print(f'Информация: {e}')
        # else:
        # Исключений не произошло, БД дропнута
        finally:
            cur.execute(f"CREATE DATABASE {database_name}")

        conn.close()
        # result = HeadHunterAPI.filter_name_company()
        with psycopg2.connect(dbname=database_name, **params) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE company ( 
                        id_company SERIAL PRIMARY KEY,
                        name_company VARCHAR(255) NOT NULL,
                        url TEXT
                        )
                """)

            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE vacancy (
                        vacancy_id SERIAL PRIMARY KEY,
                        id_company REFERENCE company(id_company),
                        url TEXT
                        salary INTEGER DEFAULT 0,
                        )
                """)

            conn.commit()
            conn.close()
    @staticmethod
    def connect_to_db(query, params=params):
        conn = psycopg2.connect(dbname='postgres', **params)
        cur = conn.cursor()
        conn.autocommit = True
        cur.execute(params)
        result = cur.fetchall()
        return result

params = config()
print(DBConnector.create_database('vacancy', params))