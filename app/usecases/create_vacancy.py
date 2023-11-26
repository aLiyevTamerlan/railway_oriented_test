from stories import story, arguments, Success, Failure, Result
from app.models import Vacancy


class CreateVacancy:
    @story
    @arguments('args')
    def create(I):
        I.validate_inputs
        I.fetch_user
        I.fetch_category
        I.create_vacancy
        I.finish

    def validate_inputs(self, ctx):
        if (isinstance(ctx.args.get("vacancy_title"), str) and 
            isinstance(ctx.args.get("vacancy_title"), str) and
            isinstance(ctx.args.get("email"), str) and
            isinstance(ctx.args.get("category"), str)):
            return Success()
        return Failure(reason="not_validated")


    def fetch_user(self, ctx):
        ctx.user = self.user_repo.fecth_user_by_email(email=ctx.args.get("email"))
        return Success() if ctx.user else Failure(reason="user_exist")
    

    def fetch_category(self, ctx):
        ctx.category = self.category_repo.feth_category(name = ctx.args.get("category"))
        return Success() if ctx.category else Failure(reason="category_exist")
    

    def create_vacancy(self, ctx):
        ctx.new_vacancy = Vacancy.objects.create(
            vacancy_title = ctx.args.get("vacancy_title"),
            vacancy_content = ctx.args.get("vacancy_title"),
            vacancy_category = ctx.category,
            vacancy_author = ctx.user
            )
        return Success() if ctx.new_vacancy else Failure(reason="repo_error")
    

    def finish(self, ctx):
        return Result(ctx.new_vacancy)
        
CreateVacancy.create.failures([
    'not_validated', 
    'user_exist',
    'category_exist',
    'repo_error'
])
   
    