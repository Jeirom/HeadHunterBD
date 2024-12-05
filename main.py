from configparser import Error

import psycopg2
from src.vacancy import Vacancy

def save_to_bd(vacancies, database, params):
    conn = psycopg2.connect(dbname=database, **params)


    with conn.cursor() as cur:
        try:
            for vac in vacancies:
                vac_get = Vacancy.__dict__
                company_name = vac_get.get('employer')
                employer_url = vac_get.get('employer_url')
                cur.execute('''
                    INSERT INTO company (company_name, company_url)
                    VALUES (%s, %s)
                    ON CONFLICT (company_name) DO NOTHING
                    RETURNING company_id;                    
                ''', (company_name, employer_url)
                            )
            try:
                company_id = cur.fetchone()[0]
            except Exception as e:
                print(f'Error {e}')

                cur.execute(
                    """INSERT INTO vacancies (
                    company_id,
                    vacancy_name,
                    city,
                    salary_from,
                    salary_to,
                    currency,
                    requirement,
                    responsibility,
                    schedule,
                    employment,
                    url
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (
                        company_id,
                        vac_get.get("title"),
                        vac_get.get("city"),
                        vac_get.get("salary_from"),
                        vac_get.get("salary_to"),
                        vac_get.get("currency"),
                        vac_get.get("requirement"),
                        vac_get.get("responsibility"),
                        vac_get.get("schedule"),
                        vac_get.get("employment"),
                        vac_get.get("url"),
                    ),
                )
                conn.commit()
        except Exception as ex:
            print(f'Error {ex}')

        finally:
            conn.close()