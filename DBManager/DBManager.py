from src.create_database import DBConnector

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

    @staticmethod
    def get_vacancies_with_keyword(self, search_word):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python."""
        execute_message = f"""SELECT * FROM vacancy WHERE vacancy_name is({search_word})"""
        return self.connect_to_db(execute_message)