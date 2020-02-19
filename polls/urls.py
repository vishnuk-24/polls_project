from django.urls import path
from .import views as polls_view

urlpatterns = [

    path('index/', polls_view.index, name='index'),

]
