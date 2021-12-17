from django.contrib import admin
from .models import Question, Answer, Category, User, Quiz, History

# Register your models here.
admin.site.register(Question)

admin.site.register(Answer)

admin.site.register(Category)

admin.site.register(User)

admin.site.register(Quiz)

admin.site.register(History)
