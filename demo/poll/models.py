from tkinter import CASCADE

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from pip._internal.download import user_agent


class Question(models.Model):
    title = models.TextField(null=True, blank=True)
    status = models.CharField(default='inactive',max_length=10)

    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    #For Showing multiple choices
    @property
    def choices(self):
        return self.choice_set.all()


class Choice(models.Model):
    question = models.ForeignKey('poll.Question', on_delete=CASCADE)
    text = models.TextField(null=True, blank= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    def votes(self):
        return self.answer_set.count()


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    choice = models.ForeignKey(Choice, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name + '-' + self.choice.text








