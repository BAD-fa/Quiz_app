from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quiz(models.Model):
    name = models.CharField(max_length=255, null=True)
    quiz = models.JSONField()


class Question(models.Model):
    title = models.TextField()
    correct_answer = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title


class Answer(models.Model):
    title = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.question.title


class User(models.Model):
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class History(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.DO_NOTHING, null=True)
    answers = models.JSONField(default=dict)
    score = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.quiz.name}----{self.user.username}"
