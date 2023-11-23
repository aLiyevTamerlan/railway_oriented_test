from app.repository import VacancyRepository, UserRepository, CategoryRepository
from app.usecases.create_vacancy import CreateVacancy
from app.usecases.create_user import CreateUser
from app.usecases.create_category import CreateCategory
user_repo = UserRepository()
vacancy_repo = VacancyRepository()
category_repo = CategoryRepository()

create_user = CreateUser()
create_user.user_repo = user_repo


create_vacancy = CreateVacancy()
create_vacancy.vacancy_repo = vacancy_repo
create_vacancy.user_repo = user_repo
create_vacancy.category_repo = category_repo

create_category = CreateCategory()
create_category.category_repo = category_repo