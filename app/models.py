from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    vacancy_title = models.CharField(max_length=100)
    vacancy_content = models.CharField(max_length=100)
    vacancy_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    vacancy_author = models.ForeignKey(User, on_delete=models.CASCADE)
