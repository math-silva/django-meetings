from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .forms import NewMeetingForm
from .models import Meeting

def detail(request, pk):
    meeting = get_object_or_404(Meeting, pk=pk)

    return render(request, 'meeting/detail.html', {
        'meeting': meeting
        })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewMeetingForm(request.POST)

        # User cannot be in two meetings at the same time
        participants = form.data.getlist('participants')
        users = []
        for participant in participants:
            users.append(User.objects.get(id=participant).username)
       
        meetings = Meeting.objects.filter(
                                    date=form.data['date'], 
                                    start_time__lte=form.data['start_time'], 
                                    end_time__gte=form.data['start_time'],
        )
        for meeting in meetings:
            meeting_users = [user.username for user in meeting.participants.all()]
            for user in users: # iter through participants
                if user in meeting_users: # if user is in meeting
                    error =  f'{user} are already in a meeting at this time.'
                    messages.error(request, error)
                    return render(request, 'meeting/meeting.html', {
                        'form': form,
                        'title': 'New Meeting',
                        'error': error
                    })

        if form.is_valid():
            meeting = form.save(commit=False)
            meeting.created_by = request.user
            meeting.save()
            form.save_m2m() # Add selected participants to meeting

            return redirect('meeting:detail', pk=meeting.id)
    
    else:
        form = NewMeetingForm()

    return render(request, 'meeting/meeting.html', {
        'form': form,
        'title': 'New Meeting'
    })

@login_required
def delete(request, pk):
    meeting = get_object_or_404(Meeting, pk=pk, created_by=request.user)
    meeting.delete()

    return redirect('core:index')

@login_required
def complete(request, pk):
    meeting = get_object_or_404(Meeting, pk=pk)
    user = request.user
    if user in meeting.participants.all():
        meeting.is_complete = True
        meeting.save()
        messages.success(request, 'Meeting completed successfully.')
    else:
        messages.error(request, 'You are not a participant of this meeting.')
    return redirect('core:index')