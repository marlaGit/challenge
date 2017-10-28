from django.shortcuts import get_object_or_404,redirect, render
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
from rest_framework import viewsets
from questionnaire.serializers import *
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from rest_framework import permissions
from .forms import UserForm
import random
import matplotlib
import numpy as np



"""
Using ViewSet to generate views for REST API
"""

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer
	permission_classes = (permissions.AllowAny,)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class QuestionViewSet(viewsets.ModelViewSet):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer

class QuestionnaireViewSet(viewsets.ViewSet):
	queryset = Questionnaire.objects.all()
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	def list(self, request):
		serializer = QuestionnaireSerializer(self.queryset, many=True)

		questionnaires_struct = []
		for questionnaire in self.queryset:
			questionnaire_struct = {}
			questionnaire_struct['questionnaire']=questionnaire
			questionnaire_struct['first_question']=Question.objects.filter(questionnaire=questionnaire.pk).first()
			questionnaires_struct.append(questionnaire_struct)
		return render(request,'list_questionnaire.html',{'questionnaires':questionnaires_struct})
	def retrieve(self, request, pk=None):
		questionnaire = get_object_or_404(self.queryset, pk=pk)
		serializer = QuestionnaireSerializer(questionnaire)
		questions=[]
		print (pk)
		for question in Question.objects.filter(questionnaire=pk):
			question_struct={}
			question_struct['question_text']=question.text
			question_struct['choices']=[]
			for choice in Choice.objects.filter(question=question.pk):
				question_struct['choices'].append(choice)
			questions.append(question_struct)				
		return render(request,'questionnaire.html',{'questionnaire':questionnaire, 'questions':questions, 'user':request.user})

class LeaningViewSet(viewsets.ModelViewSet):
	queryset = Leaning.objects.all()
	serializer_class = LeaningSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
	queryset = Choice.objects.all()
	serializer_class = ChoiceSerializer

"""
function for login. if user is superuser
will be redirect to admin page. if user is already registered 
and credials are correct, user will be redict to the page with the list
of the questionnaires
"""
def login_user(request):
	logout(request)
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_superuser:
				login(request, user)
				return HttpResponseRedirect('/admin/')
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('list-questionnaires-list'))
		else:
			return HttpResponse("Username o password wrong")
	return render(request,'login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')

def create_new_user(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			new_user = User.objects.create_user(**form.cleaned_data)
			login(request,new_user)
			return HttpResponseRedirect(reverse('list-questionnaires-list'))
	else:
		form = UserForm() 
	return render(request, 'adduser.html', {'form': form}) 


class UserChoiceViewSet(viewsets.ViewSet):
	queryset = UserChoice.objects.all()
	permission_classes = (permissions.AllowAny,)

	def create(self, request):
		if request.user.pk is None:
			return HttpResponseRedirect(reverse('login'))
		user = get_object_or_404(User, pk=request.user.pk)
		answer = get_object_or_404(Choice, pk=request.POST.get('choice_pk'))
		question=answer.question
		questionnaire=question.questionnaire
		next_question=None
		question_found=False
		for q in Question.objects.filter(questionnaire=questionnaire.pk).order_by('pk'):
			if question_found==True:
				next_question=q
				break
			if q==question:
				question_found=True
		is_last_question=False
		if next_question==None:
			is_last_question=True
		previous_user_choice=UserChoice.objects.filter(user=user,answer__question=question)
		if len(previous_user_choice)>0:
			previous_user_choice.delete()
		if user.is_authenticated:
			serializer = UserChoiceSerializer(data={'answer':answer.pk,'user':user.pk})
			serializer.is_valid(raise_exception=True)		
			serializer.save()
		if is_last_question ==False:
			return redirect('/questionnaires/'+str(questionnaire.pk)+'/question/'+str(next_question.pk))
		else:
			return redirect(reverse('result', args=(questionnaire.pk,)))

def question_from_questionnaire(request,pk,pk_question):
	queryset = Questionnaire.objects.all()
	questionnaire = get_object_or_404(queryset,pk=pk)
	queryset_question= Question.objects.all().filter(questionnaire=pk)
	question = get_object_or_404(queryset_question,pk=pk_question)
	question_struct={}
	question_struct['question_text']=question.text
	question_struct['choices']=[]
#	previous_user_choice=UserChoice.objects.filter(user=request.user.pk,answer__question=question)
	for choice in Choice.objects.filter(question=question.pk):
		question_struct['choices'].append(choice)
	return render(request,'questionnaire.html',{'questionnaire':questionnaire, 'question':question_struct})

def pie_result(request,pk):
	from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
	from matplotlib.figure import Figure

	leanings={}
	labels=[]
	nvotes=[]
	nvote_tot=0
	for userchoice in UserChoice.objects.filter(user=request.user.pk):
		if userchoice.answer.question.questionnaire.pk==int(pk):
			if userchoice.answer.leaning.text in leanings.keys():
				leanings[userchoice.answer.leaning.text]=leanings[userchoice.answer.leaning.text]+1
			else:
				leanings[userchoice.answer.leaning.text]=1
			nvote_tot+=1
			
	for leaning, nvote in leanings.items():
		percentage=nvote/nvote_tot*100
		labels.append(leaning+" %.1f %%" %percentage)
		nvotes.append(nvote)

	fig = Figure()
	ax = fig.add_subplot(111, aspect='equal')
	ax.pie(nvotes, labels=labels,) 
	
	canvas=FigureCanvas(fig)
	response=HttpResponse(content_type="image/png")
	canvas.print_png(response)
	return response

def result(request,pk):
	questionnaire=get_object_or_404(Questionnaire,pk=pk)
	
	return render(request,'result.html',{'questionnaire':questionnaire})





	



