from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from app.forms import CreatePoll
from app.models import Poll


def index(request):
    polls = Poll.objects.all()
    context = {
        'polls' : polls
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        form = CreatePoll(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
            form = CreatePoll()

    context = {'form' : form }

    return render(request, 'create.html', context)


def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option1_count += 1
        elif selected_option == 'option2':
            poll.option2_count += 1
        elif selected_option == 'option3':
            poll.option3_count += 1
        else:
            HttpResponse(400, 'Invalid')

        poll.save()
        return redirect('results', poll.id)

    context = {
        'poll' : poll
    }

    return render(request, 'vote.html', context)


def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll': poll
    }

    return render(request, 'results.html', context)
