import psycopg2
from src.create_database import DBConnector
from typing import Any
class DBManager(DBConnector):

    def __init__(self):
        super().__init__()

    def get_companies_and_vacancies_count(self):
        """Метод для получения из базы данных названия компании и количества вакансий этой компании"""
        execute_message = """SELECT employers.company_name, 
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

    @staticmethod
    def save_data_to_database(data: list[dict[str, Any]], database_name: str, params: dict):
        """Сохранение данных о каналах и видео в базу данных."""

        conn = psycopg2.connect(dbname=database_name, **params)

        with conn.cursor() as cur:
            for channel in data:
                channel_data = channel['channel']['snippet']
                channel_stats = channel['channel']['statistics']
                cur.execute(
                    """
                    INSERT INTO channels (title, views, subscribers, videos, channel_url)
                    VALUES (%s, %s, %s, %s, %s)
                    RETURNING channel_id
                    """,
                    (channel_data['title'], channel_stats['viewCount'], channel_stats['subscriberCount'],
                     channel_stats['videoCount'], f"https://www.youtube.com/channel/{channel['channel']['id']}")
                )
                channel_id = cur.fetchone()[0]
                videos_data = channel['videos']
                for video in videos_data:
                    video_data = video['snippet']
                    cur.execute(
                        """
                        INSERT INTO videos (channel_id, title, publish_date, video_url)
                        VALUES (%s, %s, %s, %s)
                        """,
                        (channel_id, video_data['title'], video_data['publishedAt'],
                         f"https://www.youtube.com/watch?v={video['id']['videoId']}")
                    )

        conn.commit()
        conn.close()