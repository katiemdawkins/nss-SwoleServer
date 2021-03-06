"""swole URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from swoleapi.views import ExerciseNoteView, register_user, login_user
from rest_framework import routers
from django.conf.urls import include
from swoleapi.views.ExerciseView import ExerciseView
from swoleapi.views.SwoleUserView import SwoleUserView
from swoleapi.views.TagView import TagView

from swoleapi.views.TrainingLogView import TrainingLogView
from swoleapi.views.BodyPartView import BodyPartView
from swoleapi.views.CategoryView import CategoryView
from swoleapi.views.ExerciseInSessionView import ExerciseInSessionView
from swoleapi.views.ExerciseNoteView import ExerciseNoteView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'training_log', TrainingLogView, 'training_log')
router.register(r'exercises_in_session', ExerciseInSessionView, 'exercise_in_session')
router.register(r'exercises', ExerciseView, 'exercise')
router.register(r'categories', CategoryView, 'category')
router.register(r'body_parts', BodyPartView, 'body_part')
router.register(r'exercise_notes', ExerciseNoteView, 'exercise_note')
router.register(r'tags', TagView, 'tag')
router.register(r'swoleUsers', SwoleUserView, 'swoleUser')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('', include(router.urls)),
]
