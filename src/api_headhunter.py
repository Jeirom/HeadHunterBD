import requests
from typing import List, Dict

from main import user_input


class HeadHunterAPI:
    """Класс для работы с hh.ru"""

    def __init__(self):
        """Инициализатор"""
        self.__base_url = "https://api.hh.ru/vacancies"

    def _connect(self) -> None:
        """Метод получения запроса.  Обратите внимание на обработку ошибок!"""
        try:
            response = requests.get(self.__base_url, timeout=10) # Add timeout for robustness
            response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
        except requests.exceptions.RequestException as e:
            raise Exception(f"Ошибка подключения к API: {e}")
        except Exception as e:
            raise Exception(f"Непредвиденная ошибка: {e}")


    def get_vacancies(self, per_page: int = 20) -> List[Dict]:
        """Метод получения вакансий по ключевому слову"""
        try:
            self._connect()
            # params = {"text": "", "per_page": per_page}
            response = requests.get(self.__base_url, timeout=10) # Add timeout
            response.raise_for_status() # Check for bad status codes
            result = response.json().get("items", [])
            return result
        except requests.exceptions.RequestException as e:
            raise Exception(f"Ошибка запроса к API: {e}")
        except (KeyError, ValueError) as e:
            raise Exception(f"Ошибка обработки ответа API: {e}")  # Handle JSON parsing errors

    @staticmethod
    def filter_name_company():
        user_company = input('Введите название компаний: ')
        new_vacancy_list = []
        vacancies = HeadHunterAPI.get_vacancies
        for item in vacancies:
            if item['employer']['name'] in user_company:
                new_vacancy_list.append(item)

# test = ('БелОптовик', 'Рост Развитие Решение')
# api = HeadHunterAPI()
# vacancies = api.get_vacancies()
# print(vacancies)
# test1 = []
# for i in vacancies:
#     if i['employer']['name'] in test:
#         test1.append(i)
# print(test1)
