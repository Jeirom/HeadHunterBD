import os
import psycopg2

class DBConnector:

    def __init__(self):
        self._host = os.getenv("host")
        self._username = os.getenv("user")
        self._port = os.getenv("port")
        self._password = os.getenv("password")

    @staticmethod
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

    def connect_to_db(self, query, params=None):
        conn = psycopg2.connect(host=self._host,
                                user=self._username,
                                port=self._port,
                                password=self._password)
        cur = conn.cursor()
        conn.autocommit = True
        cur.execute(query, params)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result