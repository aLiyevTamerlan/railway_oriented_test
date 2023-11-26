from stories import story, arguments, Success, Failure, Result

class CreateUser:

    @story
    @arguments('args')
    def create(I):
        I.validate_inputs
        I.check_user
        I.create_user
        I.finish

    def validate_inputs(self, ctx):
        if (isinstance(ctx.args.get('email'), str) and
            isinstance(ctx.args.get('username'), str) and
            isinstance(ctx.args.get('password'), str)):

            return Success()
        return Failure(reason="not_validated")
    
    def check_user(self, ctx):
        user = self.user_repo.fecth_user_by_email(email=ctx.args.get('email'))
        
        return Failure(reason="user_exists") if user else Success() 


    def create_user(self, ctx):
        ctx.new_user = self.user_repo.create_user(
            email = ctx.args.get('email'),
            username = ctx.args.get('username'),
            password = ctx.args.get('password')
        )
        return Success() if ctx.new_user else Failure(reason="repo_error")
    
    def finish(self, ctx):
        return Result(ctx.new_user)
    
CreateUser.create.failures(["not_validated", "user_exists",  "repo_error"])