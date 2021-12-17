from django.shortcuts import render
from .models import Question, History, Category, User, Quiz
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import random
import json

@csrf_exempt
def create_quiz(request, username):
    # try:
        user = User.objects.get(username=username)
        quiz = Quiz(name="This quiz is for", quiz={})
        if request.method == "GET":
            temp_quiz = {}
            main_quiz = {"q": []}
            categories = Category.objects.all()
            for elm in categories:
                temp_quiz[elm.name] = {}
                questions = list(elm.question_set.all())
                random_question = random.sample(questions, 4)
                for q in random_question:
                    main_quiz["q"].append(q.id)
                    answers = list(q.answer_set.values_list("title", flat=True))
                    temp_quiz[elm.name][q.title] = answers

            try:
                history = History.objects.get(quiz__quiz=main_quiz)
                return create_quiz(request, username)

            except:
                quiz.quiz = main_quiz
                quiz.save()
                History.objects.create(quiz=quiz, user=user)
                return JsonResponse({"message": "ok", "quiz": temp_quiz})

        elif request.method == "POST":
            answer_sheet = json.loads(request.body.decode("utf-8"))
            history = History.objects.filter(user=user).last()
            score = 0
            for elm, qid in zip(answer_sheet, history.quiz.quiz["q"]):
                q = Question.objects.get(id=qid)
                history.answers[q.title] = answer_sheet[elm]
                if answer_sheet[elm] == q.correct_answer:
                    score += 5
            history.score = score
            history.save()
            return JsonResponse({"message": "ok", "score": score})

    # except:
    #     return JsonResponse({"message": "username doesn't exist"}, status=404)
