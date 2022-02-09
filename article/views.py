from django.http import HttpResponse
from django.shortcuts import render
import random
import string


class MyClass:
    string = ''

    def __init__(self, s):
        self.string = s


def index(request):
    return render(request, 'index.html')


def main_acricles(request):
    return render(request, 'main_acricles.html')

def first(request):
    return render(request, 'first.html')

def users(request):
    return render(request, 'user.html')

def article_number(request, article_id):
    num = article_id % 2
    return render(request, 'article_number.html', {'num': num})

def article_number_archive(request, article_id):
    return HttpResponse(f"This is article_number_id_archive #{article_id}.")

def article_number_slug(request, article_id, slug_text=''):
    num = article_id % 2
    text = slug_text

    return render(request, 'article_number_slug.html', {'num': num, 'text': text})


def users_number(request, users_id):
    return HttpResponse(f"This is users_number_id #{users_id}.")

def random_page(request):
    pages = ['first.html', 'article_number.html', 'article_number_slug.html', 'user.html']
    rnd_page = pages[random.randint(0, 3)]
    return render(request, rnd_page)


def random_slug(request):
    letters = string.ascii_lowercase
    pages = ['article_number.html', 'article_number_slug', 'user.html']
    rnd_page = pages[random.randint(0, 2)]
    rnd_slug = ''.join(random.choice(letters) for i in range(random.randint(5,10)))
    return render(request, rnd_page, {
        'text': rnd_slug})




