from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    designation_choices = (
        ('student', 'STUDENT'),
        ('teacher', 'TEACHER')
    )
    # user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    
    # fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    designation = models.CharField(max_length=7, choices=designation_choices, default='student')

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name_plural = 'Profile'


class Student(models.Model):
    # user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    
    # fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    hours_watched = models.FloatField(max_length=100)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name_plural = 'Students'


class Course(models.Model):
    course_name = (
        ('CompSci', 'ComputerScience'),
        ('Math-course1', 'Maths 101'),
        ('WebDev', 'Website Development'),
        ('AI', 'Intro to AI'),
        ('FOML', 'Fundamentals of Machine Learning'),
        ("DBMS", "Database Managment Services")
    )
    course_name = models.CharField(max_length=100, choices=course_name, default='default_course')
    username = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(max_length=400)
    resource_link = models.CharField(max_length=50)  # link to any notebooks/notes
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name_plural = "Courses"


# quiz

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quizzes(models.Model):
    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"
        ordering = ["id"]

    title = models.CharField(max_length=255, default=(
        "New Quiz"), verbose_name="Quiz Title")
    category = models.ForeignKey(
        Category, default=1, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Updated(models.Model):
    date_updated = models.DateTimeField(
        verbose_name="Last Updated", auto_now=True)

    class Meta:
        abstract = True


class Question(Updated):
    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ["id"]

    SCALE = (
        (0, 'Fundamental'),
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
        (4, 'Expert')
    )

    quiz = models.ForeignKey(
        Quizzes, related_name='question', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, verbose_name="Title")
    difficulty = models.IntegerField(
        choices=SCALE, default=0, verbose_name="Difficulty")
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name="Date Created")
    is_active = models.BooleanField(
        default=False, verbose_name="Active Status")

    def __str__(self):
        return self.title


class Answer(Updated):
    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
        ordering = ["id"]

    question = models.ForeignKey(
        Question, related_name='answer', on_delete=models.DO_NOTHING)
    answer_text = models.CharField(
        max_length=255, verbose_name="Answer Text")
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
