from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from questionnaire import views

#Using router to automatically create URLs for the REST API for users, groups, questions and questionnaires
router = routers.DefaultRouter()
router.register(r'userchoices', views.UserChoiceViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'questionnaires', views.QuestionnaireViewSet, 'list-questionnaires')
router.register(r'leanings', views.LeaningViewSet)
router.register(r'choices', views.ChoiceViewSet)

#create a schemas for the REST API
schema_view = get_schema_view(title='Questionnaire API')


urlpatterns = [
	url(r'^$',views.login_user),
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^login/$', views.login_user, name='login'),
	url(r'^logout/$', views.logout_view, name='logout'),
	url(r'^adduser/',views.create_new_user, name='create_user'),
	url(r'^schema/$', schema_view),
	url(r'^questionnaires/(?P<pk>[0-9]+)/question/(?P<pk_question>[0-9]+)$', views.question_from_questionnaire),
	url(r'^questionnaires/(?P<pk>[0-9]+)/result.png$', views.pie_result, name="pie_result"),
	url(r'^questionnaires/(?P<pk>[0-9]+)/result/$', views.result, name="result"),
	url(r'^admin/', admin.site.urls),
]
