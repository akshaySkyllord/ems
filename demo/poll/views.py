from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import Http404
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="/login/")
def index(request):
    context = {}
    questions = Question.objects.all()
    context['title'] = 'polls'
    context['questions'] = questions
    return render(request, 'poll/index.html', context)


@login_required(login_url="/login/")
def details(request,id=None):
    context = {}
    try:
        question = Question.objects.get(id=id)

    except:
        raise Http404
    context['question'] = question
    return render(request, 'poll/details.html', context)


@login_required(login_url="/login/")
def poll(request,id=None):
    if request.method == 'GET':
        context = {}
        try:
            question = Question.objects.get(id=id)

        except:
            raise Http404
        context['question'] = question
        return render(request, 'poll/poll.html', context)
    if request.method == 'POST':
        user_id = 1
        data = request.POST
        print("akshay" , data )
        ret = Answer.objects.create(user_id=user_id, choice_id=data['choice'])
        if ret:
            return HttpResponse("Data posted success")
        else:
            return HttpResponse("Data not posted")

