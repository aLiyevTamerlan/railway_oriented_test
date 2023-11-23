from stories import story, arguments, Success, Failure, Result
from app.models import Category

class CreateCategory:

    @story
    @arguments('args')
    def create(I):
        I.validate_inputs
        I.check_category_exist
        I.create_category
        I.finish


    def validate_inputs(self, ctx):
        if isinstance(ctx.args.get('name'), str):
            return Success()
        return Failure(reason='not_validated')
    

    def check_category_exist(self, ctx):
        category = self.category_repo.feth_category(name = ctx.args.get('name'))

        return Failure(reason="category_exists") if category else Success()
    
    
    def create_category(self, ctx):
        ctx.new_category = self.category_repo.create_category(name = ctx.args.get('name'))
        return Success() if ctx.new_category else Failure(reason="repo_error")
    

    def finish(self, ctx):
        return Result(ctx.new_category)


CreateCategory.create.failures(["not_validated", "category_exists",  "repo_error"])