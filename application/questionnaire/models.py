from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.shortcuts import redirect
from django.urls import reverse
"""
Model for user and group.
are from django auth.models
"""	
class Questionnaire(models.Model):
	"""
	Model for a questionnaire.
	One questionnaire is related to many Question and to many Leaning
	"""
	title = models.CharField("Enter the questionnaire Title", max_length=200)	
	class Meta:
		verbose_name = 'Questionnaire'
		verbose_name_plural = 'Questionnaires'	
	def create_question(self):
		link= "<a href='/admin/questionnaire/question/add/?questionnaire="+str(self.pk)+"'> New question </a>"
		return mark_safe(link)
	def existing_questions(self):
		existing_questions=""
		for i,question in enumerate(Question.objects.filter(questionnaire=self.pk)):
			existing_questions+=question.text
			if i!=len(Question.objects.filter(questionnaire=self.pk)):
				existing_questions+="<br>"
		return mark_safe(existing_questions)
	def __str__(self):
		return self.title

class Question(models.Model):
	"""
	Model for a question.
	One question is related to one Questionnaire and many Choice.
	"""
	questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
	text = models.CharField("Enter the question's text", max_length=500)
	class Meta:
		verbose_name = 'Question'
		verbose_name_plural = 'Questions'
	def __str__(self):
		return self.questionnaire.title+": "+self.text

class Leaning(models.Model):
	"""
	Model for a leaning (what is infered from the user's answers).
	One leaning is related to one Questionnaire and many Choice.
	"""
	questionnaire = models.ForeignKey(Questionnaire)
	text = models.CharField("Enter the leaning's text", max_length=200)
	class Meta:
		verbose_name = 'Leaning'
		verbose_name_plural = 'Leanings'
	def __str__(self):
		return self.questionnaire.title+": "+self.text

class Choice(models.Model):
	"""
	Model for a choice (what is infered from the user's answers).
	One choice is related to one Question, one Leaning and many UserChoice.
	"""
	question = models.ForeignKey(Question)
	leaning = models.ForeignKey(Leaning)
	text = models.CharField("Enter the choice's text",max_length=500)
	class Meta:
		verbose_name = 'Choice'
		verbose_name_plural = 'Choices'
	def __str__(self):
		return self.question.text+": "+self.text+"->"+self.leaning.text

class UserChoice(models.Model):
	"""
	Model for an answer of one user to one question.
	One Userchoice is related to one Choice and one User.
	Information on device is included as well.
	"""
	answer = models.ForeignKey(Choice)
	user = models.ForeignKey(User)
	deviceType=models.CharField(max_length=50, blank=True, null=True)
	deviceFamily=models.CharField(max_length=50, blank=True, null=True)
	deviceBrand=models.CharField(max_length=50, blank=True, null=True)
	deviceModel=models.CharField(max_length=50, blank=True, null=True)
	browserFamily=models.CharField(max_length=50, blank=True, null=True)
	browserVersion=models.CharField(max_length=50, blank=True, null=True)
	osFamily=models.CharField(max_length=50, blank=True, null=True)
	osVersion=models.CharField(max_length=50, blank=True, null=True)
	def __str__(self):
		return self.user.username+" question: "+str(self.answer.question)+" answer: "+self.answer.text+" "+self.answer.leaning.text

