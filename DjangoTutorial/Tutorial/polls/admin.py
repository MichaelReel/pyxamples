from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields' : ['question_text']}),
        ('Date Information',{'fields' : ['pub_date']})
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)