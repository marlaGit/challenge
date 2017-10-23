from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers

"""
Using Serializer to enable REST API for User, Group, Question, Questionnaire,
Leaning, Choice
"""

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Question
		fields = ('questionnaire', 'text')

class QuestionnaireSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Questionnaire
		fields = ('title',)

class LeaningSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Leaning
		fields = ('questionnaire', 'text')

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Choice
		fields = ('question', 'leaning', 'text')
