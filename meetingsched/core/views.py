from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from meeting.models import Meeting
from .forms import SignUpForm, LoginForm
from datetime import datetime, timedelta

current_date = datetime.now().date()

def index(request):
    meetings = Meeting.objects.order_by('is_complete', 'date', 'start_time')

    global current_date
    current_date = datetime.now().date()
    return render(request, 'core/index.html', {
        'meetings': meetings,
        'current_date': current_date
    })

def date(request, op):
    meetings = Meeting.objects.order_by('is_complete', 'date', 'start_time')
 
    global current_date
    if op == 'next':
        current_date = current_date + timedelta(days=1)
    else:
        current_date = current_date - timedelta(days=1)
    return render(request, 'core/index.html', {
        'meetings': meetings,
        'current_date': current_date
    })

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

@user_passes_test(lambda u: u.is_staff)
def user_management_view(request):
    users = User.objects.all()
    return render(request, 'core/users.html', {
        'users': users
    })

@user_passes_test(lambda u: u.is_staff)
def remove_user(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect('core:users')