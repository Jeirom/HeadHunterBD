from src.api_headhunter import HeadHunterAPI
from DBManager.DBManager import DBManager
import psycopg2
def main():
    print('Привет, user!')
    api = HeadHunterAPI
    vacancy_list = api.filter_name_company() # Здесь будут лежать выбранные вакансии юзера.
    print(vacancy_list)


if __name__ == '__main__':
    main()
