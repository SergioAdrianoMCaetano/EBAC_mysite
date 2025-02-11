# myapp/views.py

from django.http import HttpResponse

def minha_view(request):
    return HttpResponse("Olá, essa é a minha view!")

