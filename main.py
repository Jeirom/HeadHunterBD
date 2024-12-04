import sqlite3
from src.api_headhunter import HeadHunterAPI
from DBManager.DBManager import DBManager
import psycopg2

# def save_to_bd(data, database, params):
#     conn = psycopg2.connect(dbname=database, **params)
#
#     with conn.cursor() as cur:
#         for vac in data:
#             # employee = vac['id']['employee']
#             employer_name = vac['employer']['name']
#             cur.execute(
#                 """
#                 INSERT INTO vacancy (name_company) VALUES (%s) RETURNING vacancy_id
#                 """,
#                 (employer_name)
#             )
#
#             vacancy_id = cur.fetchone()[0]
#     conn.commit()
#     conn.close()
#
# data = [{'id': '111495155', 'premium': False, 'name': 'Менеджер по оптовым продажам', 'department': None, 'has_test': False, 'response_letter_required': False, 'area': {'id': '11228', 'name': 'Тарасово (Минская область)', 'url': 'https://api.hh.ru/areas/11228'}, 'salary': {'from': 2000, 'to': 5000, 'currency': 'BYR', 'gross': False}, 'type': {'id': 'open', 'name': 'Открытая'}, 'address': {'city': 'деревня Тарасово', 'street': 'улица Мира', 'building': '1', 'lat': 53.919245, 'lng': 27.407015, 'description': None, 'raw': 'деревня Тарасово, улица Мира, 1', 'metro': None, 'metro_stations': [], 'id': '15201130'}, 'response_url': None, 'sort_point_distance': None, 'published_at': '2024-11-21T10:40:40+0300', 'created_at': '2024-11-21T10:40:40+0300', 'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=111495155', 'show_logo_in_search': None, 'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/111495155?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/111495155', 'relations': [], 'employer': {'id': '10801717', 'name': 'БелОптовик', 'url': 'https://api.hh.ru/employers/10801717', 'alternate_url': 'https://hh.ru/employer/10801717', 'logo_urls': {'240': 'https://img.hhcdn.ru/employer-logo/6565738.png', '90': 'https://img.hhcdn.ru/employer-logo/6565737.png', 'original': 'https://img.hhcdn.ru/employer-logo-original/1236325.png'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=10801717', 'accredited_it_employer': False, 'trusted': True}, 'snippet': {'requirement': 'Что желательно иметь кандидату: - Быть уверенным пользователем ПК (google docs, любая crm). - Энергичность, высокий уровень эмпатии, душевность и уверенность в...', 'responsibility': 'Развивать клиентскую базу и увеличивать объемы продаж. Консультировать клиентов по товарам и услугам компании. Проводить презентации продукции и предлагать решения...'}, 'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [], 'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False, 'professional_roles': [{'id': '70', 'name': 'Менеджер по продажам, менеджер по работе с клиентами'}], 'accept_incomplete_resumes': False, 'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'}, 'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False, 'adv_context': None}]
# params = {'host': 'localhost',
#           'user': 'postgres',
#           'password': 123456789,
#           'port': 5432,
#           'client_encoding': 'utf=8'}
# save_to_bd(data, 'new',params)

import psycopg2

def save_to_bd(data, database, params):
    conn = psycopg2.connect(dbname=database, **params)

    try:
        with conn.cursor() as cur:
            for vac in data:
                try:
                    employer_name = vac['employer']['name'] # Get employer name
                    cur.execute(
                        """
                        INSERT INTO company (name_company) VALUES (%s);
                        """,
                        (employer_name,)  # Correct: employer_name is already a string
                    )
                    # vacancy_id = cur.fetchone()[0]
                    # print(f"Vacancy ID {vacancy_id} inserted for {employer_name}") #Confirmation message
                except (KeyError, TypeError) as e:
                    print(f"Error processing vacancy: {e}") #Handles missing or incorrect data

        conn.commit()
        print("Data inserted successfully.")
    except psycopg2.Error as e:
        print(f"Database error: {e}")
        conn.rollback() # Rollback in case of database errors
    finally:
        if conn:
            conn.close()
database = 'new'
params = {'host': 'localhost',
          'user': 'postgres',
          'password': '123456789', #password should be a string
          'port': 5432,
          'client_encoding': 'utf8'}
conn = psycopg2.connect(dbname=database, **params)
cur = conn.cursor()
employer_name = 'test'
cur.execute("""INSERT INTO company (name_company) VALUES (%s);""",(employer_name,))
cur.execute("""INSERT INTO company (name_company) VALUES (%s);""",(employer_name,))
cur.execute("""INSERT INTO company (name_company) VALUES (%s);""",(employer_name,))
conn.commit()
cur.close()
conn.close()


# Correct: employer_name is already a string)
# data = [{'id': '111495155', 'premium': False, 'name': 'Менеджер по оптовым продажам', 'department': None, 'has_test': False, 'response_letter_required': False, 'area': {'id': '11228', 'name': 'Тарасово (Минская область)', 'url': 'https://api.hh.ru/areas/11228'}, 'salary': {'from': 2000, 'to': 5000, 'currency': 'BYR', 'gross': False}, 'type': {'id': 'open', 'name': 'Открытая'}, 'address': {'city': 'деревня Тарасово', 'street': 'улица Мира', 'building': '1', 'lat': 53.919245, 'lng': 27.407015, 'description': None, 'raw': 'деревня Тарасово, улица Мира, 1', 'metro': None, 'metro_stations': [], 'id': '15201130'}, 'response_url': None, 'sort_point_distance': None, 'published_at': '2024-11-21T10:40:40+0300', 'created_at': '2024-11-21T10:40:40+0300', 'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=111495155', 'show_logo_in_search': None, 'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/111495155?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/111495155', 'relations': [], 'employer': {'id': '10801717', 'name': 'БелОптовик', 'url': 'https://api.hh.ru/employers/10801717', 'alternate_url': 'https://hh.ru/employer/10801717', 'logo_urls': {'240': 'https://img.hhcdn.ru/employer-logo/6565738.png', '90': 'https://img.hhcdn.ru/employer-logo/6565737.png', 'original': 'https://img.hhcdn.ru/employer-logo-original/1236325.png'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=10801717', 'accredited_it_employer': False, 'trusted': True}, 'snippet': {'requirement': 'Что желательно иметь кандидату: - Быть уверенным пользователем ПК (google docs, любая crm). - Энергичность, высокий уровень эмпатии, душевность и уверенность в...', 'responsibility': 'Развивать клиентскую базу и увеличивать объемы продаж. Консультировать клиентов по товарам и услугам компании. Проводить презентации продукции и предлагать решения...'}, 'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [], 'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False, 'professional_roles': [{'id': '70', 'name': 'Менеджер по продажам, менеджер по работе с клиентами'}], 'accept_incomplete_resumes': False, 'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'}, 'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False, 'adv_context': None}]
# params = {'host': 'localhost',
#           'user': 'postgres',
#           'password': '123456789', #password should be a string
#           'port': 5432,
#           'client_encoding': 'utf8'}
# save_to_bd(data, 'new',params)