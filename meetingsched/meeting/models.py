from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
import datetime

class Meeting(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField('meeting date')
    start_time = models.TimeField('start time', default="00:00:00")
    end_time = models.TimeField('end time', default="00:00:00")
    location = models.CharField(max_length=200)
    agenda = models.CharField(max_length=200)
    participants = models.ManyToManyField(User)
    is_complete = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meetings', default=1)
    
    class Meta:
        verbose_name_plural = 'Meetings'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending times must after starting times.')
        