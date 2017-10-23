from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from questionnaire import views
from questionnaire import models 

#Using router to automatically create URLs for the REST API for users, groups, questions and questionnaires
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'questionnaires', views.QuestionnaireViewSet)
router.register(r'leanings', views.LeaningViewSet)
router.register(r'choices', views.ChoiceViewSet)
#create a schemas for the REST API
schema_view = get_schema_view(title='Questionnaire API')


urlpatterns = [
	url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^schema/$', schema_view),
    url(r'^admin/', admin.site.urls),
]
