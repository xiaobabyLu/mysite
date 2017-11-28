# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {}
    values = {'id':1,'name':'bruce bruce  django.template.exceptions.TemplateSyntaxError: Invalid filte','age':28}
    context['test'] = 'This a header test!'
    context['values'] =values
    return render(request, 'index.html', context)