from django.contrib import admin
from django.shortcuts import redirect 
from .models import Question, Leaning, Choice, Questionnaire, UserChoice




class UserChoiceAdmin(admin.ModelAdmin):
	model = UserChoice
	fieldsets= [
		('answer', {'fields':['answer','user']})
	]
	
	list_display=('__str__',
		'deviceType','deviceFamily','deviceBrand','deviceModel',
		'browserFamily','browserVersion',
		'osFamily', 'osVersion',
		'ipAddress', 'ipCountry','ipCity','ipGPSLatitude','ipGPSLongitude')
	


class ChoiceInline(admin.TabularInline):
	"""
	used in QuestionAdmin
	"""
	model = Choice
	fieldsets = [
		('Create the choices for the question',{'fields':['text', 'leaning']})
	]
	def formfield_for_foreignkey(self,db_field,request,**kwargs):
		"""
		used for filter the leanings related to the questionnaire
		"""
		if db_field.name== "leaning":
			pk_questionnaire=request.GET.get('questionnaire')
			kwargs["queryset"] = Leaning.objects.filter(questionnaire=pk_questionnaire)
		return super(ChoiceInline, self).formfield_for_foreignkey(db_field,request,**kwargs)

class QuestionAdmin(admin.ModelAdmin):
	"""
	Do not add Question directly from admin main page.
	Use New question link from questionnaires admin page
	TODO: replace admin main page to avoid any mistake
	"""
	fieldsets = [
		('Question', {'fields':['questionnaire', 'text']})
	]
	inlines = [
		ChoiceInline,
	]
	list_display = ('get_edit_url',)
	"""
	Redifine response_add and response_change to redirect to 
	questionnaires admin page
	"""
	def response_add(self, request, obj, post_url_continue=None):
		return redirect('/admin/questionnaire/questionnaire/')
	def response_change(self, request, obj):
		return redirect('/admin/questionnaire/questionnaire/')

class LeaningInline(admin.TabularInline):
	"""
	Used in Questionnaire
	"""
	model = Leaning

class QuestionnaireAdmin(admin.ModelAdmin):
	fieldsets = [
		('Questionnaire', {'fields': ['title']})
	]
	inlines = [
		LeaningInline,		
	]
	show_change_link = True
	list_display = ('title', 'existing_questions', 'create_question',)

admin.site.register(UserChoice, UserChoiceAdmin)	
admin.site.register(Question, QuestionAdmin)
admin.site.register(Questionnaire, QuestionnaireAdmin)



