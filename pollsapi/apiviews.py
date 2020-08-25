"""Pollsapi apiview."""

from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import authenticate
# from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .models import Poll, Choice, Vote
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer, UserSerializer


class LoginView(APIView):
    """APIView for authenticate users."""

    permission_classes = ()

    def post(self, request,):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            # login(request, user)
            return Response({'token': user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class UserCreate(generics.CreateAPIView):
    """View for create User object."""

    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class PollList(generics.ListCreateAPIView):
    "PollList from ListCreateAPIView"

    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollDetail(generics.RetrieveDestroyAPIView):
    """PollDetail from RetrieveDestroyAPIView"""

    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class ChoiceList(generics.ListCreateAPIView):
    """ChoiceList from ListCreateAPIView."""

    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs["pk"])
        return queryset
    serializer_class = ChoiceSerializer


class CreateVote(APIView):
    """CreateVote from APIView"""
    
    def post(self, request, pk, choice_pk):
        """Create vote."""
        voted_by = request.data.get("voted_by")
        data = {'choice': choice_pk, 'poll': pk, 'voted_by': voted_by}
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PollViewSet(viewsets.ModelViewSet):
    """PollViewSet using ModelViewSet."""

    queryset = Poll.objects.all()
    serializer_class = PollSerializer


"""
class PollList(APIView):
    "APIView for poll list."

    def get(self, request):
        "return latest 20 poll objects"

        polls = Poll.objects.all()[:20]
        data = PollSerializer(polls, many=True).data
        return Response(data)

class PollDetail(APIView):
    "APIView for poll details."

    def get(self, request, pk):
        "Poll instance"

        poll = get_object_or_404(Poll, pk=pk)
        data = PollSerializer(poll).data
        return Response(data)
"""