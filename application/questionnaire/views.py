from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import viewsets
from questionnaire.serializers import *

"""
Using ViewSet to generate views for REST API
"""

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class QuestionViewSet(viewsets.ModelViewSet):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer

class QuestionnaireViewSet(viewsets.ModelViewSet):
	queryset = Questionnaire.objects.all()
	serializer_class = QuestionnaireSerializer

class LeaningViewSet(viewsets.ModelViewSet):
	queryset = Leaning.objects.all()
	serializer_class = LeaningSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
	queryset = Choice.objects.all()
	serializer_class = ChoiceSerializer
	
	


