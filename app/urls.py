from django.urls import path
from app.views import CreateVcancyAPIView, CreateUserAPIView, CreateCategoryAPIView
urlpatterns = [
    path('', CreateVcancyAPIView.as_view()),
    path('users/', CreateUserAPIView.as_view()),
    path('category/', CreateCategoryAPIView.as_view())
]