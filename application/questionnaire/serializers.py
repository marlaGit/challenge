from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers

"""
Using Serializer to enable REST API for User, Group, Question, Questionnaire,
Leaning, Choice
"""

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = ('questionnaire', 'text')

class QuestionnaireSerializer(serializers.ModelSerializer):
	class Meta:
		model = Questionnaire
		fields = ('title',)

class LeaningSerializer(serializers.ModelSerializer):
	class Meta:
		model = Leaning
		fields = ('questionnaire', 'text')

class ChoiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Choice
		fields = ('question', 'leaning', 'text')

class UserChoiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserChoice
		fields = ('answer', 'user',
 			'deviceType','deviceFamily','deviceBrand','deviceModel',
			'browserFamily','browserVersion',
			'osFamily', 'osVersion',
			'ipAddress', 'ipCountry','ipCity','ipGPSLatitude','ipGPSLongitude')

