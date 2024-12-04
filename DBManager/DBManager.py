import psycopg2

from config import config
from src.create_database import DBConnector, params
from typing import Any
from src.api_headhunter import HeadHunterAPI
class DBManager(DBConnector):

    def __init__(self):
        super().__init__()

    def get_companies_and_vacancies_count(self):
        """Метод для получения из базы данных названия компании и количества вакансий этой компании"""
        execute_message = """SELECT * FROM company, 
        COUNT(vacancies.employer_id)
        FROM employers JOIN vacancies 
        USING (employer_id) GROUP BY employer_id"""
        return self.connect_to_db(execute_message)


    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию."""
        execute_message = """SELECT employers.company_name, vacancy.vacancy_name, vacancy.salary, vacancy.link"""
        return self.connect_to_db(execute_message)


    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям."""
        execute_message = """SELECT AVG(salary) FROM employers"""
        return self.connect_to_db(execute_message)


    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        execute_message = """SELECT salary FROM employers WHERE salary > SUM(salary)/COUNT(salary)"""
        return self.connect_to_db(execute_message)


    def get_vacancies_with_keyword(self, search_word):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python."""
        execute_message = f"""SELECT * FROM vacancy WHERE vacancy_name is({search_word})"""
        return self.connect_to_db(execute_message)

    def save_data_to_db(self):
        """Записывает данные в базу данных."""
        params = {'host': 'localhost',
                  'user': 'postgres',
                  'password': 123456789,
                  'port': 5432,
                  'client_encoding': 'utf=8'}
        # db = DBConnector
        # result = db.create_database('new', params)
        api = HeadHunterAPI
        vacancies = api.filter_name_company()
        # params = config()
        params = {'host': 'localhost',
                  'user': 'new',
                  'password': 123456789,
                  'port': 5432,
                  'client_encoding': 'utf=8'}
        conn = psycopg2.connect(dbname='postgres', **params)

        with conn.cursor() as cur:
            try:
                for vacancy in vacancies:
                    print(vacancy)
                    vac_dict = vacancy.__dict__
                    company_name = vac_dict.get("employer")
                    employer_url = vac_dict.get("employer_url")
                    """ Заполняем таблицу companies"""
                    cur.execute(
                        """
                        INSERT INTO company (name_company, company_url)
                        VALUES (%s, %s)
                        ON CONFLICT (company_name) DO NOTHING
                        RETURNING company_id;
                        """,
                        (
                            company_name,
                            employer_url,
                        ),
                    )
                    try:
                        company_id = cur.fetchone()[0]
                    except Exception:
                        pass

                    """ Заполняем таблицу vacancies"""
                    cur.execute(
                        """INSERT INTO vacancies (
                        vacancy_id,
                        url,
                        salary
                        )
                        VALUES (%s, %s, %s)""",
                        (
                            company_id,
                            vac_dict.get("salary_to"),
                            vac_dict.get("url"),
                        ),
                    )
                    conn.commit()
            except Exception as ex:
                print(ex)
                conn.rollback()
            finally:
                conn.close()

db = DBManager.save_data_to_db
print(db)