from src.api_headhunter import HeadHunterAPI
from src.vacancy import Vacancy


def get_vacancies_from_hh() -> list[dict]:
    """Возвращает список словарей с вакансиями с hh.ru.
    В список попадут только те вакансии, компании которых есть в списке сompany names"""

    company_names = ("БелОптовик", "Яндекс Команда для бизнеса", "Ozon", "VK", "Студия Лебедева", "ГазПром", "Лукойл",
                     "Сбербанк", "Т-Банк", "Slumberger")
    api = HeadHunterAPI()
    vacancies = api.get_vacancies()
    print(vacancies)
    list_for_bd = []
    for item in vacancies:
        employer = item.get("employer")["name"]
        for company_name in company_names:
            if company_name.lower() in employer.lower():
                employer_url = item.get("employer")["alternate_url"]
                title = item["name"]
                city = item.get("area")["name"]
                employment = item.get("employment")["name"]
                if item["salary"]:
                    salary = item["salary"]
                    currency = salary.get("currency")
                    if salary["from"]:
                        salary_from = salary["from"]
                    else:
                        salary_from = 0
                    if salary["to"]:
                        salary_to = salary["to"]
                    else:
                        salary_to = 0
                else:
                    salary_from = 0
                    salary_to = 0
                    currency = "RUR"
                url = item["alternate_url"]
                vacancy = Vacancy(
                    employer,
                    employer_url,
                    title,
                    city,
                    salary_from,
                    salary_to,
                    currency,
                    employment,
                    url,
                )
                list_for_bd.append(vacancy)

    return list_for_bd


