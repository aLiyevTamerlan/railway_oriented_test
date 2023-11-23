from app.models import User, Category, Vacancy

class VacancyRepository:

    def create_vacancy(
            self,
            vacancy_title: str,
            vacancy_content: str,
            vacancy_category: Category,
            vacancy_author: User) -> Vacancy:
        
        new_vacancy = Vacancy.objects.create(
            vacancy_title = vacancy_title,
            vacancy_content=vacancy_content,
            vacancy_category=vacancy_category,
            vacancy_author=vacancy_author)
        
        return new_vacancy
    

class UserRepository:

    def create_user(
            self,
            username: str,
            email: str,
            password: str
    ) -> User:
        user = User.objects.create(username = username, email = email)
        user.set_password(password)
        user.save()
        return user
    

    def fecth_user_by_email(
            self,
            email:str
    ):
        user = User.objects.filter(email=email).first()
        return user
    
    def fetch_all_users(
            self
    ):
        user = User.objects.all()
        return user


class CategoryRepository:

    def create_category(
            self,
            name: str) -> Category:
        
        new_category = Category.objects.create(
            name = name)
        
        return new_category
    
    def feth_category(
            self,
            name: str
    ):
        category = Category.objects.filter(name = name).first()
        
        return category