from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        # fields= '__all__'
        fields = ["course_name","description", "resource_link"]
        