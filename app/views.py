from django.shortcuts import render
from rest_framework.views import APIView
# from returns.result import Result, Failure, Success
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from app.implemented import create_vacancy, create_user, create_category
from app.serializers import UserSerializer, CategorySerializer
# Create your views here.


class CreateVcancyAPIView(APIView):
    
    def post(self, request):
        
        v = create_vacancy.create.run(args = request.data)
        if v.is_success:
            success = True
            result = 'Good.'
        elif v.failed_because('not_validated'):
            result = 'Data not validated.'
        # print(v)
        # if v.failed_because("not_valid"):
        #     print("Tamerlan")
        return Response(result)
    

class CreateUserAPIView(APIView):
    
    @swagger_auto_schema(responses={200: UserSerializer}, request_body=UserSerializer)
    def post(self, request):

        u = create_user.create.run(args = request.data)
        stat = status.HTTP_400_BAD_REQUEST
        if u.is_success:
            success = True
            result = 'Good.'
            stat = status.HTTP_201_CREATED

        elif u.failed_because('not_validated'):
            success = False
            result = 'not_validated'
            

        elif u.failed_because('user_exists'):
            success = False
            result = 'user_exists'

        elif u.failed_because('repo_error'):
            success = False
            result = 'repo_error'

        return Response({'success': success, 'result': result}, status=stat)
    

class CreateCategoryAPIView(APIView):

    @swagger_auto_schema(responses={200: CategorySerializer}, request_body=CategorySerializer)
    def post(self, request):
        c = create_category.create.run(args = request.data)
        stat = status.HTTP_400_BAD_REQUEST
        if c.is_success:
            success = True
            result = 'Good.'
            stat = status.HTTP_201_CREATED

        elif c.failed_because('not_validated'):
            success = False
            result = 'not_validated'
            

        elif c.failed_because('category_exists'):
            success = False
            result = 'category_exists'
        elif c.failed_because('repo_error'):
            success = False
            result = 'repo_error'

        return Response({'success': success, 'result': result}, status=stat)
