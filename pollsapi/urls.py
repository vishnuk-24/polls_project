"""Pollsapi urls."""

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from django.urls import path, re_path

from .apiviews import PollViewSet
from .import views
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote, UserCreate, LoginView

router = DefaultRouter()
router.register('polls', PollViewSet, 'polls')


app_name = 'pollsapi'

urlpatterns = [
    # path("polls/", views.polls_list, name="polls_list"),
    # path("polls/<int:pk>/", views.polls_detail, name="polls_detail"),

    path("login/", LoginView.as_view(), name="login"),
    # path("login/", views.obtain_auth_token, name="login"),
    path("users/", UserCreate.as_view(), name="user_create"),

    path("polls-api/", PollList.as_view(), name="api-polls_list"),
    path("polls-api/<int:pk>/", PollDetail.as_view(), name="api-polls_detail"),
    path("choices-api/", ChoiceList.as_view(), name="api-choice_list"),
    path("vote-api/", CreateVote.as_view(), name="api-create_vote"),
    path("polls-api/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls-api/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
]

urlpatterns += router.urls

"""

• Use viewsets.ModelViewSet when you are going to allow all or most of CRUD operations on a model.
• Use generics.* when you only want to allow some operations on a model
• Use APIView when you want to completely customize the behaviour.

"""