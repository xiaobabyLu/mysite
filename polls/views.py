from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from .models import Question,Choice
from django.urls import reverse
from django.views import generic
from polls.forms import QuestionForm,UserRegisterForm,UserLoginForm
from polls.models import User
from django.contrib.auth.decorators import login_required
import os
from django.contrib import auth


def register(request):
    if request.method == 'POST':
        uf = UserRegisterForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            email = uf.cleaned_data['email']

            user = User()
            user.username = username
            user.password = password
            user.email = email
            user.save()
            return render_to_response('polls/register_success.html',{'username': username})
    else:
        uf = UserRegisterForm()
    return render_to_response('polls/register.html',{'uf':uf})


def login(request):
    if request.method == 'POST':
        uf = UserLoginForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = auth.authenticate(username__exact=username,password__exact=password)
            if user:
                return render_to_response('polls/login_success.html',{'username':username})
            else:
                return HttpResponseRedirect('/polls/login/')
    else:
        uf = UserLoginForm()
    return render_to_response('polls/login.html',{'uf':uf})


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/polls/login/')


@login_required
def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "do not select a choice", })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:6]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


@login_required
def form_input(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            Question = form.save()
            Question.save()
            return HttpResponseRedirect(reverse("polls:index"))
    else:
        form = QuestionForm()
    FILE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(request, os.path.join(FILE_ROOT, 'polls/templates/polls','input.html'),{'form':form})