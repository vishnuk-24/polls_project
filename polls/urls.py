"""Polls urls."""

from django.urls import path
from .import views as polls_view

app_name = 'polls'

urlpatterns = [
    path('', polls_view.IndexView.as_view(), name='index'),
    path('<int:pk>/', polls_view.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', polls_view.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', polls_view.vote, name='vote'),
]

"""
urlpatterns = [

    path('', polls_view.index, name='index'),

    path('<int:question_id>/', polls_view.detail, name='detail'),

    path('<int:question_id>/results/', polls_view.results, name='results'),

    path('<int:question_id>/vote/', polls_view.vote, name='vote'),

    path('articles/<int:year>/', polls_view.year_archive),

    # path('articles/<int:year>/<int:month>/', polls_view.month_archive),

    # path('articles/<int:year>/<int:month>/<int:pk>/', polls_view.article_detail)
]
"""