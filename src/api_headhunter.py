import requests
from typing import List, Dict


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
            response = requests.get(self.__base_url, timeout=10)  # Add timeout
            response.raise_for_status()  # Check for bad status codes
            return response.json().get("items", [{}])  # Возвращает список словарей вместо списка элементов
        except requests.exceptions.RequestException as e:
            raise Exception(f"Ошибка запроса к API: {e}")
        except (KeyError, ValueError) as e:
            raise Exception(f"Ошибка обработки ответа API: {e}")  # Handle JSON parsing errors


