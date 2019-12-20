from django.contrib import admin
from .models import Question,Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display=["id","question_text"]
admin.site.register(Question)
admin.site.register(Choice)
# Register your models here.
