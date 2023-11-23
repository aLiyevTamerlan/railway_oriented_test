from stories import story, arguments, Success, Failure, Result




class CreateVacancy:
    @story
    @arguments('args')
    def create(I):
        I.validate_inputs
        # I.fetch_user
        # I.fetch_category
        # I.create_vacancy
        I.finish

    def validate_inputs(self, ctx):
        if isinstance(ctx.args.get("vacancy_title"), str) and False:
            return Success()
        return Failure(reason="not_validated")

    
    def finish(self, stage):
        return Result("asd")
        
CreateVacancy.create.failures([
    'not_validated', 
])
   
    