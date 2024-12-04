from src.api_headhunter import HeadHunterAPI
import psycopg2


def filter_name_company():
    user_company = [
    'Яндекс', 'Газпром', 'Вконтакте', 'VK', 'Тинькофф', 'Ozon', 'Авито', 'Lamoda', 'Контур', 'Холдинг Т1', 'БелОптовик']
    new_vacancy_list = []
    api = HeadHunterAPI()
    vacancies = api.get_vacancies()

    for item in vacancies:
        if item['employer']['name'] in user_company:
            new_vacancy_list.append(item)
    return new_vacancy_list


def connect_to_db(query, params):
    conn = psycopg2.connect(dbname='postgres', **params)
    cur = conn.cursor()
    conn.autocommit = True
    cur.execute(query, params)
    result = cur.fetchall()
    return result
