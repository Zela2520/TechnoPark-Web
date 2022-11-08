from django.shortcuts import redirect, render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def question_page(request, question_id: int):
    return render(request, 'question_page.html')


def ask(request):
    return render(request, 'ask.html')


def hot(request):
    return render(request, 'hot.html')


def tag(request):
    return render(request, 'tag.html')


def settings(request):
    return render(request, 'settings.html')


def authorization(request):
    return render(request, 'authorization.html')


def registration(request):
    return render(request, 'registration.html')
