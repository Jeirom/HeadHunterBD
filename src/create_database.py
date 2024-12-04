import psycopg2

from main import params


class DBCreator:

    params = {'host': 'localhost',
              'user': 'postgres',
              'password': 123456789,
              'port': 5432,
              'client_encoding': 'utf=8'}

    def __init__(self, db_name: str, params: dict):
        self.db_name = db_name
        self.params = params

    def create_db(self):
        """Создает базу данных."""

        """ Подключаемся к  PostgreSQL"""
        conn = psycopg2.connect(dbname="postgres", **self.params)
        conn.autocommit = True
        cur = conn.cursor()

        """ Создаем базу данных """
        cur.execute(f"DROP DATABASE IF EXISTS {self.db_name};")
        cur.execute(f"CREATE DATABASE {self.db_name};")
        conn.close()


    def create_database(self):
        """Создает таблицы в базе данных."""
        # Подключаемся к БД
        conn = psycopg2.connect(dbname=self.db_name, **self.params)

        with conn.cursor() as cur:
            cur.execute(
                """ CREATE TABLE companies (
                    company_id SERIAL PRIMARY KEY, 
                    company_name VARCHAR(255) NOT NULL UNIQUE,
                    company_url TEXT
                )"""
            )

        with conn.cursor() as cur:
            cur.execute(
                """
                    CREATE TABLE vacancies (
                        vacancy_id SERIAL PRIMARY KEY,
                        company_id INT REFERENCES companies(company_id),
                        vacancy_name VARCHAR NOT NULL,
                        city VARCHAR(100) NOT NULL,
                        salary_from INT,
                        salary_to INT,
                        currency VARCHAR(5),
                        employment VARCHAR(30),
                        url TEXT
                    )"""
            )
        conn.commit()
        conn.close()


con1 = DBCreator('postgres1', params)
con1.create_database()