import psycopg2

from config import config
from src.create_database import DBCreator
from src.filling_in_the_DB import get_vacancies_from_hh
from src.vacancy import Vacancy
from DBManager import DBManager


loading = (
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
    "loading",
)


# def connect_to_db(query, params):
#     """ Функция подключения к базе данных """
#     conn = psycopg2.connect(dbname="postgres", **params)
#     cur = conn.cursor()
#     conn.autocommit = True
#     cur.execute(query, params)
#     result = cur.fetchall()
#     return result

def submenu() -> int:
    """Реализация подменю, возвращает номер меню"""

    print(
        "2 - Получить список всех компаний и количество вакансий у каждой компании. \n"
        "3 - Получить список всех вакансий.\n"
        "4 - Получить среднюю зарплату по вакансиям.\n"
        "5 - Получить список всех вакансий, у которых зарплата выше средней.\n"
        "6 - Получить список вакансий по ключевым словам.\n"
        "8 - Выход.\n"
    )

    while True:
        answer = input("Выберите действие: ").strip()
        if answer.isdigit():
            answer = int(answer)
            if 1 <= answer <= 8:
                break
            else:
                print("Можно ввести только число от 1 до 8!")
        else:
            print("Можно ввести только целое число")
    print("*" * 50)
    return answer


def user_interaction() -> None:
    """Основная функция по взаимодействию с пользователем"""

    while True:
        answer = submenu()
        if answer == 2:
            db = DBManager()
            db.get_companies_and_vacancies_count()
        elif answer == 3:
            db = DBManager()
            db.get_all_vacancies()
        elif answer == 4:
            db = DBManager()
            db.get_avg_salary()
        elif answer == 5:
            db = DBManager()
            db.get_vacancies_with_higher_salary()
        elif answer == 6:
            keywords = input("Введите слова через запятую: ").split(",")
            db = DBManager()
            db.get_vacancies_with_keyword(keywords)
        elif answer == 8:
            print("Благодарим за использование программы.\n      До свидания.")
            break


def save_to_bd(vacancies, database, params):
    """ Функция сохранения данных в DATABASE """
    # params = {
    #     "host": "localhost",
    #     "user": "postgres",
    #     "password": 123456789,
    #     "port": 5432,
    #     "client_encoding": "utf=8",
    # }
    params = config()
    conn = psycopg2.connect(dbname=database, **params)

    with conn.cursor() as cur:
        try:
            for vac in vacancies:
                vac_get = Vacancy.__dict__
                company_name = vac_get.get("employer")
                employer_url = vac_get.get("employer_url")
                cur.execute(
                    """
                    INSERT INTO company (company_name, company_url)
                    VALUES (%s, %s)
                    ON CONFLICT (company_name) DO NOTHING
                    RETURNING company_id;                    
                """,
                    (company_name, employer_url),
                )
            try:
                company_id = cur.fetchone()[0]
            except Exception as e:
                print(f"Error {e}")

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
            print(f"Error {ex}")

        finally:
            conn.close()


def welcome_script_next(db_name, params):
    """ Вторая функция для взаимодействия с юзером. """
    # user_choice = input(
    #     'Впишите интересующие компании через запятую/nИли напишите < 1 > для использования стандартного '
    #     'набора компаний в поиске вакансий(Рекомендуется!).')
    # if user_choice == 1:
    vacancy = get_vacancies_from_hh()
    print("Вакансии получены")
    print("*" * 50)
    print("Вакансии и компании записываются в базу данных.. ожидайте.")

    # params = {
    #     "host": "localhost",
    #     "user": "postgres",
    #     "password": 123456789,
    #     "port": 5432,
    #     "client_encoding": "utf=8",
    # }
    params = config()
    save_to_bd(vacancy, db_name, params)
    waiting = 1
    for i in loading:
        print("*" * waiting)
        waiting += 1
    user_interaction() # переводим юзера на функционал выбора действий с данными


# else:
#     print('Другие варианты тестируются.')
#     waiting = 1
#     for i in loading:
#         print('*' * waiting)
#         waiting += 1
#     print('Всего доброго!')


def welcome_script():
    """ Первая функция для взаимодействия с юзером. """

    print("*" * 50)
    print(
        "Привет! Эта программа посвящена курсовой работе. О ней ты можешь узнать больше в README.md"
    )
    print("*" * 50)
    user_choice = int(
        input(
            "Для создания базы данных напиши < 1 >/nДля выхода из программы напиши < 2 > : "
        )
    )
    db_name = input("Введите название для вашей БД: ")
    #
    # params = {
    #     "host": "localhost",
    #     "user": "postgres",
    #     "password": 123456789,
    #     "port": 5432,
    #     "client_encoding": "utf=8",
    # }
    params = config()
    if user_choice == 2:
        print("Такие ответы мы не принимаем!")
    # try:
    elif user_choice == 1:
        DBCreator(db_name, params)
        print("База данных успешно создана с Вашими параметрами.")
    # except Exception:
    #     print('Возникла ошибка. Возможно, БД с таким именем уже существует!')

    welcome_script_next(db_name, params) # запускаем вторую часть кода интерфейса
