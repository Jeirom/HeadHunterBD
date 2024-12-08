class Vacancy:
    """Класс вакансий. Принимает в себя данные с filling_in_the_DB, отправляет данные в бд"""
    def __init__(
        self,
        employer,
        employer_url,
        title,
        city,
        salary_from,
        salary_to,
        currency,
        employment,
        url,
    ):
        self.employer = employer
        self.employer_url = employer_url
        self.title = title
        self.city = city
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.employment = employment
        self.url = url
