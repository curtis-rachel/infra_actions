"""Определение view-функций для приложения infra."""
from django.http import HttpResponse


def index(request):
    """View-фунция первой страницы."""
    return HttpResponse('У меня получилось!')


def second_page(request):
    """View-фунция второй страницы."""
    return HttpResponse('А это вторая страница')
