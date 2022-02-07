from django.http import HttpResponse

def main(request):
    return HttpResponse("Home Page")

def main_acricles(request):
    return HttpResponse('This is page for acricles')

def acricles_archive(request):
    return HttpResponse('This is page for acrticles_archive ')

def users(request):
    return HttpResponse('USERS')

def article_number(request, article_id):
    return HttpResponse(f"This is article_number_id #{article_id}.")

def article_number_archive(request, article_id):
    return HttpResponse(f"This is article_number_id_archive #{article_id}.")

def article_number_text(request, article_id, slug_text=''):
    return HttpResponse(  "Arcticle ID is: {}. {}".format(article_id, "Article name is: {}".format(slug_text)
        if slug_text else "This is unnamed article!!!"))

def users_number(request, users_id):
    return HttpResponse(f"This is users_number_id #{users_id}.")
