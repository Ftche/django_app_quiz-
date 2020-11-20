from django.urls import path, include
from quiz import views

from rest_framework import routers

from quiz.views import ExamQuestionViewset
from quiz.views import QuestionViewset, ExamViewset

router = routers.DefaultRouter()
router.register('question',QuestionViewset)
router.register('exam',ExamViewset)

urlpatterns = [
    # path('', views.contact , name = "contact"),
    path('api/',include(router.urls)),
    path('',views.welcome,name="welcome"),
    path('create/',views.create_user,name="create_user"),
    path('validate_login/',views.log_in,name="log_user"),
    path('add_exam/',views.add_exam,name="add_exam"),
    path('add_question/',views.add_question,name="add_question"),
    path('test',views.get_data,name="getdata"),
    path('logout',views.log_out,name="log_out"),
]