from django.contrib import admin

# Register your models here.
from app.models import *


admin.site.register(Category)

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['vacancy_title', 'vacancy_content', 'vacancy_category', 'vacancy_author']

