"""Polls admin"""

from django.contrib import admin

from .models import Choice, Question, Article, Reporter

admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Article)
admin.site.register(Reporter)
