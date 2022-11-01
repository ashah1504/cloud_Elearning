from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from rest_framework.response import Response

from .models import Course, Student
from .forms import CourseForm
from rest_framework import generics
from .models import Quizzes, Question
from .serializers import QuizSerializer, RandomQuestionSerializer, QuestionSerializer
# descriptive and in control
from rest_framework.views import APIView


# Create your views here.


def home(request):
    return render(request, 'index.html')


def courses(request):
    return render(request, 'courses.html')



@login_required(login_url="login_page")
def courses_after_login(request):
    print("im in courses after login")
    try: 
        student = Student.objects.get(user_name=request.user)
        print(student)   
        data = Course.objects.filter(username = student)
        context = {"course":data}
        print(context)
    except Exception as e:
        context = {"course": "data not found"}
    return render(request, 'courses_after_login.html', context)


def course_single(request, id):
    fetch_data = Course.objects.get(id=id)
    context = {"fetch_data": fetch_data}
    return render(request, 'course-single.html', context)


def courses_add(request):
    form = CourseForm()
    if request.method == 'POST':
        myData = CourseForm(request.POST)
        if myData.is_valid():
            data = myData.save(commit = False)
            data.username = Student.objects.get(user_name=request.user)
            data.save()
            return redirect('courses_after_login')
    context = {"form": form}
    return render(request, 'courses_add.html', context)



def courses_delete(request, id):
    data = Course.objects.get(id=id)
    data.delete()
    return redirect('courses_after_login')


@login_required(login_url="login_page")
# @permission_required('', login_url="home")
def teachers(request):
    return render(request, 'teachers.html')


@login_required(login_url="login_page")
def events(request):
    return render(request, 'events.html')


def aboutUs(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def news(request):
    return render(request, 'news.html')


def gallery(request):
    return render(request, "gallery.html")


class Quiz(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


# randomize and filter based on the topic
class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.all().order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class QuizQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        quiz = Question.objects.all()
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)

