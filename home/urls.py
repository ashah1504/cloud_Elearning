from django.urls import path
from . import views
from .views import Quiz, RandomQuestion, QuizQuestion

urlpatterns = [
    path("", views.home, name="home"),

    path("courses/", views.courses, name="courses"),

    path("courses_after_login/", views.courses_after_login, name="courses_after_login"),
    path("courses_single/<str:id>/", views.course_single, name="course_single"),
    path("courses_add/", views.courses_add, name="courses_add"),
    path("courses_delete/<str:id>/", views.courses_delete, name="courses_delete"),

    path("teachers/", views.teachers, name="teachers"),
    path("events/", views.events, name="events"),
    path("aboutUs/", views.aboutUs, name="aboutUs"),
    path("contact/", views.contact, name="contact"),
    path("news/", views.news, name="news"),
    path("quiz/", Quiz.as_view(), name="quiz"),
    path("quiz/r/<str:topic>/", RandomQuestion.as_view(), name='random'),
    path("quiz/q/<str:topic>/", QuizQuestion.as_view(), name='questions'),
    path("gallery/", views.gallery, name="gallery"),

]
