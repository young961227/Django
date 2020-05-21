from django.contrib import admin

from .models import Question, Choice

class Choiceinline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    inlines = [Choiceinline]

admin.site.register(Question, QuestionAdmin)