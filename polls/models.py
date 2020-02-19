"""Polls model."""

from django.db import models
from core import BaseModel


class Question(BaseModel):
    """Question model for adding questions."""

    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.question_text


class Choice(BaseModel):
    """Choice model for adding choices of each questions."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
