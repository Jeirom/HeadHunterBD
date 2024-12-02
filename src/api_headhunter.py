import requests
from typing import AnyStr

class HeadHunterAPI:
    """Класс для работы с hh.ru"""

    def __init__(self):
        """Инициализатор"""
        self.__base_url = "https://api.hh.ru/vacancies"

    def connect(self) -> None:
        """Метод получения запроса"""
        response = requests.get(self.__base_url)
        if response.status_code != 200:
            raise Exception("Не удалось подключиться к API")

    def get_vacancies(self, keyword: str, per_page: int = 20) -> AnyStr:
        """Метод получения вакансий по ключевому слову"""
        self.connect()
        params = {"text": keyword, "per_page": per_page}
        response = requests.get(self.__base_url, params=params)
        return response.json().get("items", [])