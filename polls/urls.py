"""Polls urls."""

from django.urls import path
from .import views as polls_view

urlpatterns = [

    path('', polls_view.index, name='index'),

    path('<int:question_id>/', polls_view.detail, name='detail'),

    path('<int:question_id>/results/', polls_view.results, name='results'),

    path('<int:question_id>/vote/', polls_view.vote, name='vote'),
]
